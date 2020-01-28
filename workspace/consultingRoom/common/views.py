from rest_framework.response import Response
from rest_framework import status


class GenericResponseLinked(object):
    model = None

    def convert_to_json(self, instance):
        pass

    def get_object(self, pk):
        try:
            instance = self.model.objects.get(pk=pk, deleted=False)
            return self.convert_to_json(instance)
        except self.model.DoesNotExist:
            return []

    def get(self, request, *args, **kwargs):
        return Response(self.get_object(self.kwargs['pk']))


class GenericListResponseLinked(object):
    model = None

    def get_queryset(self):
        return self.model.objects.all().filter(deleted=False)

    def convert_to_json(self, instance):
        pass

    def get_object(self):
        result_set = []
        queryset = self.get_queryset()
        for result in queryset:
            result_set.append(self.convert_to_json(result))
        return result_set

    def get(self, request,  format=None):
        return Response(self.get_object())


class GenericDeleteModel(object):
    model = None
    serializer_class = None

    def deleteModel(self, pk):
        try:
            instance = self.model.objects.get(pk=pk)
            instance_aux = instance
            instance_aux.deleted = True
            serializer = self.serializer_class(
                instance, data=instance_aux.to_json())
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except self.model.DoesNotExist:
            return Response([], status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        return self.deleteModel(self.kwargs['pk'])
