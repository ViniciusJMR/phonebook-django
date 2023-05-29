# Phonebook Project
A phonebook website using Django framework for frontend and backend.

> Disclaimer: This project was based on Udemy course [Curso de Python 3 do Básico Ao Avançado (com projetos reais)
](https://www.udemy.com/course/python-3-do-zero-ao-avancado/)
 
### How to run
```shell
git clone https://github.com/ViniciusJMR/phonebook-django.git

python -m venv venv
. venv/bin/activate 

pip install django

# Migrating Databases
python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```

### Creating a Super User to access /admin
```shell
python manage.py createsuperuser
python manage.py changepassword USERNAME
```