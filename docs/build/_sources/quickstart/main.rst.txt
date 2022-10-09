**********
Quickstart
**********

Set up the project on your local machine
----------------------------------------

1. Clone the repository:

   ``git clone https://github.com/rohitgeddam/FindMyRoomie.git``  

2. Setup the virtual environment:

   ``python -m venv venv``  

3. Activate the virtual environment:

   -  On Mac/Linux:

      ``source venv/bin/activate``  

   -  On Windows:

      ``venv\Scripts\activate``  

4. Install required modules and libraries:

   ``pip install -r requirements.txt``  

5. Run the application:  

   ::

      cd src 
      python manage.py migrate
      python manage.py runserver

After adding another field to Model
-----------------------------------

Django’s way of propagating changes you make to your models (adding a
field, deleting a model, etc.) into your database schema.

::

   python manage.py makemigrations
   python manage.py migrate

Populate fake data for testing
------------------------------

\``\` python manage.py seed_users

creates ten fake users
======================

python manage.py seed_users 10


Run test
########

In a terminal:

``cd src``

``py manage.py runserver``

Open another terminal:

``cd src``

``py manage.py test``

