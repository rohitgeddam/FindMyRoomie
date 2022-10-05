[![Test](https://github.com/rohitgeddam/CSC510_HW1/actions/workflows/build.yml/badge.svg)](https://github.com/rohitgeddam/CSC510_HW1/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/Arun152k/CSC510_HW1/branch/HW1/graph/badge.svg?token=WA4KNGKU6J)](https://codecov.io/gh/Arun152k/CSC510_HW1)
[![code_size](https://img.shields.io/github/languages/code-size/rohitgeddam/CSC510_PROJECT1)](https://github.com/rohitgeddam/CSC510_PROJECT1) 
[![repo_size](https://img.shields.io/github/repo-size/rohitgeddam/CSC510_PROJECT1)](https://github.com/rohitgeddam/CSC510_PROJECT1)</br>
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7061868.svg)](https://doi.org/10.5281/zenodo.7061868)

# FindMyRoomie 👯‍♂️


### How to setup the project on your local machine?
* `git clone https://github.com/rohitgeddam/CSC510_PROJECT1.git`
* Setup virtual environment
  * `python -m venv venv`
  * On Mac/Linux
    * `source venv/bin/activate`
  * On Windows
    * `venv\Scripts\activate`
* `pip install -r requirements.txt`
* `cd src`
* `python manage.py runserver`
* `python manage.py migrate`

## How to setup the project on your local machine?
1. Download a free Python IDE such as PyCharm, Visual Studio Code, Spyder, etc. from online.

2. In the IDE terminal copy and paste the command: 

   `git clone https://github.com/rohitgeddam/CSC510_PROJECT1.git`

3. To setup the virtual environment

   `python -m venv venv`

    * On Mac/Linux
    
      `source venv/bin/activate`
    * On Windows
    
      `venv\Scripts\activate`
   
   (If you get an error at this step, continue on.)
   
   `pip install -r requirements.txt`

   If you get an error do `pip install django`. 
   
   If you get this message "ModuleNotFoundError: No module named 'crispy_forms'" enter the command `pip install django-crispy-forms`

4. To run virtual environment

   Type into the terminal:

   `cd Roomies`

   `py manage.py runserver`
   
Click the link next to "Starting development server at " to view the project

## How to create a new webpage

Read the instructions starting from "Here we create the varied pages and assign the respective HTML files" on this webpage: https://www.geeksforgeeks.org/django-creating-a-multi-page-website/

## After adding another field to Model
Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

   `py manage.py makemigrations`
   
   `py manage.py migrate`

## Location of important files
CSS is in 

Images are in 

## Populate fake data for testing

```
python manage.py seed_users <number of fake instances>

# creates 10 fake users
python manage.py seed_users 10
```
