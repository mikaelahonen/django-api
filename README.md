# Django REST API

This is a Django and Django Rest Framerwork powered python application. 
Updates from this github repo will be automatically built by Jenkins and deployed by an Elastic Beanstalk instance in AWS.

The purpose is to learn smart development practices as well as trying to apply machine learning algorithms to my self leadership sofware.

## Django ORM
Django object relational mapping notes.

Use `values()` to limit the columns and to get the actual values instead of objects:
`ModelName.objects.all.values('author', 'date', 'slug')`

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


## Pip


### Erros
ImportError: No module named 'functions'
Try to change `from my_python_file.py import *` to `from app.my_python_file.py import *`

`Error: Microsoft Visual C++ 10.0 is required` or Cython error. 
Latest pandas package 0.21.0 was not suitable with Python 3.4.
I downgraded to pandas 0.20.3.

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