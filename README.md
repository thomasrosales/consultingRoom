# Consulting Room App

Consulting Room is a web application build in `python 3.7`, `django`, `django-rest` to the back-end and `angular` to the front-end. The application is until in construction but the first version have the follow characteristics:


```
Token Managment
DataBase Model Complete
Login and Logout
Home Page
Get List of Shedulers
```

The next setps are build the funcionality to add persons, patient and doctors using the `API REST`:

```
Add Person as a Doctor or a Patient
Modify a Person
Delete a Person
```

The bankend is allready to use and you can test it using the postman application or similar.


**Backend: [consultingRoomBE](https://github.com/thomasrosales/consultingRoom)**

**Frontend: [consultingRoomFE](https://github.com/thomasrosales/consultingRoomFE/)**


To inicializate the angular application is necessary to be in the main folder of the front-end proyect that is: consultingRoomFE/ and execute the following command:

`ng serve --proxy-config proxy.conf.json`

To inicializate the django application is neccesary to be in the back-end main folder proyect that is: consultingRoom/ amd execute the following command:


`python manage.py runserver`
