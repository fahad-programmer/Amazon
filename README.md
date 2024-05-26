# Amazon
<img src="https://github.com/fahad-programmer/Amazon/blob/main/public/Screenshot%202024-05-26%20225505.png" alt="Amazon Clone">

*This is not an actualy Amazon website Screenshot rather a clone made completly in Django.

## How To Setup
- Create A Virtual Environment in python and install all the modules from requirement.txt file `pip install -r requirements.txt`. (There maybe some issues related ugettext, well to fix it we have to change all those imports to gettext even in modules)
- Start a PostgreSQL server and create a db name `amazon-django` and update all information in `settings.py`.
- Migrate the project `python manage.py migrate`
- Run Server to view working website `python manage.py runserver`
- You can access admin by creating a superuser using `python manage.py createsuperuser` and then navigate to admin and login. Using Admin we can add new Products, Orders, and alot of other user informations.

## Remarks
This project was made in Dec 2020 during the covid period. This was a learning project for Django and its working.
