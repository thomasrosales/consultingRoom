from rest_framework import serializers
from rest_framework import status


def instance_is_deleted(instance, property):
    """
    Arguments:
        instance {[Object Model]} -- [object within property delete inside]
        property {[String]} -- [property to create a string error]

    Raises:
        serializers.ValidationError: [Object is deleted]
        serializers.ValidationError: [Exception]
    """
    ERROR_MESSAGE = "The instance with property {} => {} was deleted."
    try:
        if instance.deleted:
            instanceJson = instance.to_json()
            raise serializers.ValidationError(
                ERROR_MESSAGE.format(property, instanceJson[property]))
    except Exception as err:
        raise serializers.ValidationError(
            "Error: {0}".format(err), status.HTTP_400_BAD_REQUEST)
