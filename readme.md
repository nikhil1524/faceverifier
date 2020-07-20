

** Face Recognizer **

create schema faceverifier;
CREATE USER 'faceadmin'@'localhost' IDENTIFIED BY 'password';
grant all privileges on faceverifier.* TO 'faceadmin'@'localhost';


$ python3 manage.py makemigrations faceverifier

$ python3 manage.py sqlmigrate faceverifier 0001
$ python3 manage.py migrate


Create super user in Django
$ python manage.py createsuperuser

Run the Django server
$ python manage.py runserver

python3 manage.py collectstatic


pip install passlib