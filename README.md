## Table of Contents

- [Short Description](#short-description)
- [Project Dependencies](#project-dependencies)
- [Project Structure](#folder-structure)
- [Available Scripts](#available-scripts)


## Short Description

Simple web application with Django (SSR and REST API) applying good development practices and TDD.

## Project Dependencies

The project dependencies are listed in the requirements.txt file.

```
Django==2.0.4
pytz==2018.4

```

### Notes

Python version used is 3.6.5.

To create the virtual environment for the project, when this version of Python it is not the default in the system but it is installed, you can do:
* virtualenv -p /usr/bin/python3.6 env

### Testing tools




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



## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode. Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits. You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.

Jest has an integrated coverage reporter that works well with ES6 and requires no configuration.<br>
Run `npm test -- --coverage` to include a coverage report.

