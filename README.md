# Django REST API

This is a Django and Django Rest Framerwork powered python application.
Updates from this github repo will be automatically built by Jenkins and deployed by an Elastic Beanstalk instance in AWS.

The purpose is to learn smart development practices as well as trying to apply machine learning algorithms to my self leadership sofware.

## AWS Elastic beanstalk

### Errors

#### Old pip version
These lines occured after an attempt to install
the app to elastic beanstalk.

`You are using pip version 7.1.2, however version 9.0.1 is available.`
`Your requirements.txt is invalid`

The problem was old version of `pip`.
This probably because I included `pandas` to my packages.

I added these lines to my `.ebextensions` file and it worked:
```YAML
commands:
  pip_upgrade:
    command: /opt/python/run/venv/bin/pip install --upgrade pip
    ignoreErrors: false
```

The error was also fixed by upgrading elastic beanstalk machine to
`64bit Amazon Linux 2017.09 v2.6.0 running Python 3.4` version.

## Django ORM
Django object relational mapping notes.

Use `values()` to limit the columns and to get the actual values instead of objects:
`ModelName.objects.all.values('author', 'date', 'slug')`

## Django Rest Framework
[Additional field to model serializer](https://stackoverflow.com/questions/18396547/django-rest-framework-adding-additional-field-to-modelserializer)

## Django practices
* List model classes alphabetically in views, models and serializers.

## manage.py

### Database migrations
Create SQL scripts for database changes
according to models.py:

`python manage.py makemigrations`


Run SQL scripts from migrations files to make
the changes to database:

`python manage.py migrate`


Show selected migration file

`python manage.py sqlmigrate gym 0001`

### shell
Handy for testing the Django object API.
`python manage.py shell`

## Managers
User managers for:
* Adding extra methods
* Modify initial queryset

A custom Manager method can return anything you want. It doesn’t have to return a QuerySet.

## Pip


### Erros
ImportError: No module named 'functions'
Try to change `from my_python_file.py import *` to `from app.my_python_file.py import *`

`Error: Microsoft Visual C++ 10.0 is required` or Cython error.
Latest pandas package 0.21.0 was not suitable with Python 3.4.
I downgraded to pandas 0.20.3.

## Querysets
A queryset normally returns objects from a single model.

[Join models](https://stackoverflow.com/questions/31237042/whats-the-difference-between-select-related-and-prefetch-related-in-django-orm).

## About serveless tech
This solutions is deployed on normal Linux server.
According to my investigation here are some ideas about
serverless technologies on AWS.

### The serverless solution
* Front end by React
* Authentication by AWS Cognito
* API by AWS API Gateway
* Data processing by AWS Python 3.6 Lambda functions
* Data storage by AWS RDS or SQLite in S3

### Pros
* Modularity: API and authentication would be individual entities
* Possibly no need for Python framework
* More robust authentication
* Reduced costs for small number of users

### Cons
* Takes time to change the architecture
* Authentication still wouldn't be super simple
* AWS Api Gateway latency relatively high
* More modularity means more repetition
