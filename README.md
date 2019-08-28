# OldschoolMTGDB

*    Authors: Guillem Alomar and Lluis Cortès   
*    Current release: August 28th, 2019                     
*    Code version: 0.1                      
*    Availability: Public

## Index

* [Requirements](#requirements)
* [Documentation](#documentation)
    * [Explanation](#explanation)
* [Using the service](#using-the-service)
    * [First of all](#first-of-all)
    * [Starting the server](#starting-the-server)
    * [Accessing the service](#accessing-the-service)
* [Sources of Information](#sources-of-information)

## Requirements

Programming language
- Python +3.7

PIP packages
- Django 1.11.23
- django-widget-tweaks 1.4.1
- Markdown 2.6.9

## Documentation

### Explanation

This project consists in a platform to visualize Oldschool MTG Decks.

## Using the service

### First of all

#### Virtual environment

- I recommend creating a virtualenv for this project. Use the following commands in a terminal to install virtualenv, create a virtual environment, and activate it.
```
~/OldschoolMTGDB$ pip3 install virtualenv
~/OldschoolMTGDB$ virtualenv -p python3 venv
~/OldschoolMTGDB$ source venv/bin/activate
```
After creating it, you should run the following command to install all the pip packages required:
```
(venv) ~/OldschoolMTGDB$ pip install -r requirements.txt
```
Now all pip packages needed have been installed.
You can check your environment packages using the following command:
```
(venv) ~/OldschoolMTGDB$ pip freeze
```

#### Database set up

You now need to initialize the database with the following commands:
```
(venv) ~/OldschoolMTGDB$ python manage.py makemigrations
(venv) ~/OldschoolMTGDB$ python manage.py migrate
```

#### Admin user set up

To create an admin user for the service, type the following command in your terminal:
```
(venv) ~/OldschoolMTGDB$ python manage.py createsuperuser
```
It will ask for a username, email (not mandatory) and password.

### Starting the server

We can execute the application with the following command:
```
(venv) ~/OldschoolMTGDB$ python manage.py runserver
```
The output should be really similar to this:

```
Performing system checks...

System check identified no issues (0 silenced).
August 28, 2019 - 14:20:16
Django version 1.11.23, using settings 'oldschoolmtgdb.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Accessing the service

Now you can use a web browser to access the service on:

```
http://127.0.0.1:8000
```

To access the admin page go to:
```
http://127.0.0.1:8000/admin
```

### Sources of Information

- https://scotch.io/tutorials/build-your-first-python-and-django-application
- https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html
- https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html
- https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html
- https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html
- https://simpleisbetterthancomplex.com/series/2017/10/02/a-complete-beginners-guide-to-django-part-5.html
- https://simpleisbetterthancomplex.com/series/2017/10/09/a-complete-beginners-guide-to-django-part-6.html
- https://simpleisbetterthancomplex.com/series/2017/10/16/a-complete-beginners-guide-to-django-part-7.html
