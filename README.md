# todo-api

This is the sample todo that runs on Flask.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/berkkarahann/todo-api)

## Setup

NOTE: This is a Python3.8 Project.

### Install

Install Python3.8 if you don't have it already:

```bash
brew install python@3.8
```

Create a virtualenv for 3.8 in the project root:

```bash
virtualenv -p python3.8 venv
```

Activate the newly created virtualenv:

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Migration

Copy .env.example to .env.

```bash
cp .env.example .env
```

Initialize migration by creating a migration repository 
```bash
flask db init
```

Generate an initial migration
```bash
flask db migrate
```

Apply the changes described by the migration script to your database
```bash
flask db upgrade
```

## Launch

You can launch the todo-api by running gunicorn as follows
```bash
gunicorn manage:app
```

## Document

You can explore available endpoints in /docs endpoint via Swagger 

NOTE: Make sure you set the scheme as 'https' if you deploy the api to Heroku for Swagger tests


## Testing

You can perform todolist end-to-end test with following command
```bash
pytest
```
