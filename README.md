# Phonebook Project
A phonebook website using Django framework for frontend and backend.

> Disclaimer: This project was based on Udemy course [Curso de Python 3 do Básico Ao Avançado (com projetos reais)
](https://www.udemy.com/course/python-3-do-zero-ao-avancado/)

### About
This app simulates a contact list. You can only Create/Update/Delete
after logging in and only Update or Delete your own contacts.  
#### This project was made using Python 3.11.3.
 
### How to run
```shell
git clone https://github.com/ViniciusJMR/phonebook-django.git

python -m venv venv # Install dependencies 
. venv/bin/activate # Install dependencies
pip install -r requirements.txt # Install dependencies


python manage.py makemigrations # Migrating Databases
python manage.py migrate # Migrating Databases

python utils/create_contacts.py # Add fake contacts to database

python manage.py runserver
```

### Creating a Super User to access /admin
```shell
python manage.py createsuperuser
python manage.py changepassword USERNAME
```