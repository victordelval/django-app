## Table of Contents

- [Short Description](#short-description)
- [Project Dependencies](#project-dependencies)
- [Project Structure](#folder-structure)
- [Execution](#execution)


## Short Description

Simple web application with Django (SSR and REST API) applying good development practices and TDD.

## Project Dependencies

The project dependencies are listed in the requirements.txt file.

```
Django==2.0.4
flake8==3.5.0
mccabe==0.6.1
pep8==1.7.1
pycodestyle==2.3.1
pyflakes==1.6.0
pytz==2018.4
```

### Notes

Python version used is 3.6.5.

To create the virtual environment for the project, when this version of Python it is not the default in the system but it is installed, you can do:
* `virtualenv -p /usr/bin/python3.6 env`

Once the virtualenv is activated you can install the dependencies:
* `pip install -r requirements.txt`



### Testing tools

**unittest** Python standard library module used by Django’s unit tests. This module defines tests using a class-based approach. Django offers `django.test.TestCase`, which is a subclass of `unittest.TestCase` that runs each test inside a transaction to provide isolation.



## Project Structure

The code of the application, the "src" folder, is organized in the following directories:

```
env/
src/
    app/
        settings.py
        urls.py
        wsgi.py
    db.sqlite3
    manage.py
.gitignore
README.md
requirements.txt
```



## Execution

In the django project directory (src folder), you can run:

### `python manage.py migrate`

To run model and data migrations into the sqlite3 database.


### `python manage.py runserver`

Runs the app in the development mode. Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

The page will reload if you make edits. You will also see any errors in the console.


### `python manage.py test`

Launches all tests in the project.

To include a coverage report:
* `coverage run --source='.' manage.py test plans`
* `coverage report`

