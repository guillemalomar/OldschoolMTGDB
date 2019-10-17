# OldschoolMTGDB

*    Authors: Guillem Alomar and Lluís Cortès   
*    Current release: August 28th, 2019                     
*    Code version: 0.1                      
*    Availability: Public

## Index

- [OldschoolMTGDB](#oldschoolmtgdb)
  - [Index](#index)
  - [Requirements](#requirements)
  - [Documentation](#documentation)
    - [Explanation](#explanation)
  - [Using the service](#using-the-service)
    - [Docker environment](#docker-environment)
    - [Virtual environment](#virtual-environment)
      - [Database set up](#database-set-up)
      - [Admin user set up](#admin-user-set-up)
    - [Starting the server](#starting-the-server)
    - [Accessing the service](#accessing-the-service)
    - [Sources of Information](#sources-of-information)

## Requirements

Programming language:

* Python +3.7

PIP packages:

* beautifulsoup4 4.8.0
* Django 2.2.4
* django-widget-tweaks 1.4.5
* djongo 1.2.35
* Markdown 2.6.9
* requests 2.22.0
* sqlparse 0.2.4

Docker environment:

* Docker
* Docker-compose

## Documentation

### Explanation

This project consists in a platform to visualize Oldschool MTG Decks.

## Using the service

### Docker environment

If this is the first time you spin up the environment, you should run:

```bash
make build
```

This command will build the Docker image and start all the dependencies needed.

To simply start the environment execute `make run`

If you also want to load a set of fixtures into the database, execute the following command:

```bash
make fixtures
```

This command will load all data in `./data/files/` into MongoDB.

### Virtual environment

* I recommend creating a virtualenv for this project. Use the following commands in a terminal to install virtualenv, create a virtual environment, and activate it.
  
```bash
~/OldschoolMTGDB$ pip3 install virtualenv
~/OldschoolMTGDB$ virtualenv -p python3 venv
~/OldschoolMTGDB$ source venv/bin/activate
```

After creating it, you should run the following command to install all the pip packages required:

```bash
(venv) ~/OldschoolMTGDB$ pip install -r requirements.txt
```

Now all pip packages needed have been installed.
You can check your environment packages using the following command:

```bash
(venv) ~/OldschoolMTGDB$ pip freeze
```

#### Database set up

You now need to initialize the database with the following commands:

```bash
(venv) ~/OldschoolMTGDB$ python manage.py makemigrations
(venv) ~/OldschoolMTGDB$ python manage.py migrate
```

After this, we can load the cards data and the tournaments data:

```bash
(venv) ~/OldschoolMTGDB$ mongoimport -d decks -c decks_card data/files/os_cards.json
(venv) ~/OldschoolMTGDB$ mongoimport -d decks -c decks_tournament data/files/os_tournaments.json
```

(this step isn't ready yet, working on it)

#### Admin user set up

To create an admin user for the service, type the following command in your terminal:

```bash
(venv) ~/OldschoolMTGDB$ python manage.py createsuperuser
```

It will ask for a username, email (not mandatory) and password.

### Starting the server

We can execute the application with the following command:

```bash
(venv) ~/OldschoolMTGDB$ python manage.py runserver
```

The output should be really similar to this:

```bash
Performing system checks...

System check identified no issues (0 silenced).
August 28, 2019 - 14:20:16
Django version 1.11.23, using settings 'oldschoolmtgdb.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Accessing the service

Now you can use a web browser to access the service on:

`http://127.0.0.1:8000`

To access the admin page go to:

`http://127.0.0.1:8000/admin`

### Sources of Information

* <https://scotch.io/tutorials/build-your-first-python-and-django-application>
* <https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html>
* <https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html>
* <https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html>
* <https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html>
* <https://simpleisbetterthancomplex.com/series/2017/10/02/a-complete-beginners-guide-to-django-part-5.html>
* <https://simpleisbetterthancomplex.com/series/2017/10/09/a-complete-beginners-guide-to-django-part-6.html>
* <https://simpleisbetterthancomplex.com/series/2017/10/16/a-complete-beginners-guide-to-django-part-7.html>
