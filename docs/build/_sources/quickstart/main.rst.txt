**********
Quickstart
**********

Setup the project in your local machine:
########################################

1. Download and Install a free Python IDE such as PyCharm, Visual Studio Code,
   Spyder, etc.

2. In the IDE terminal copy and paste the command:

   ``git clone https://github.com/rohitgeddam/CSC510_PROJECT1.git``

3. To setup the virtual environment

   ``python -m venv venv``

   -  On Mac/Linux

      ``source venv/bin/activate``

   -  On Windows

      ``venv\Scripts\activate``


   (If you get an error at this step, continue on.)

   ``pip install -r requirements.txt``


   If you get an error do ``pip install django``.


   If you get this message “ModuleNotFoundError: No module named
   ‘crispy_forms’” enter the command ``pip install django-crispy-forms``

4. To run virtual environment

   Type into the terminal:

   ``cd src``

   ``python manage.py runserver``

Click the link next to “Starting development server at” to view the
project


After adding another field to Model
###################################

Django’s way of propagating changes you make to your models (adding a
field, deleting a model, etc.) into your database schema.

``py manage.py makemigrations``

``py manage.py migrate``

Populate fake data for Test
###########################
::

   python manage.py seed_users <number of fake instances>

   # creates 10 fake users
   python manage.py seed_users 10

Run test
########

In a terminal:

``cd src``

``py manage.py runserver``

Open another terminal:

``cd src``

``py manage.py test``

