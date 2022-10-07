[![Test](https://github.com/rohitgeddam/FindMyRoomie/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/rohitgeddam/FinMyRoomie/actions/workflows/unit_tests.yml)
[![codecov](https://codecov.io/gh/rohitgeddam/FindMyRoomie/branch/main/graph/badge.svg?token=PCOHJETYCD)](https://codecov.io/gh/rohitgeddam/FindMyRoomie)
[![Test](https://github.com/rohitgeddam/FindMyRoomie/actions/workflows/linting.yml/badge.svg)](https://github.com/rohitgeddam/FinMyRoomie/actions/workflows/linting.yml)
![CodeQL](https://github.com/rohitgeddam/FindMyRoomie/workflows/CodeQL/badge.svg)
[![code_size](https://img.shields.io/github/languages/code-size/rohitgeddam/CSC510_PROJECT1)](https://github.com/rohitgeddam/CSC510_PROJECT1) 
[![repo_size](https://img.shields.io/github/repo-size/rohitgeddam/CSC510_PROJECT1)](https://github.com/rohitgeddam/CSC510_PROJECT1)</br>
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7061868.svg)](https://doi.org/10.5281/zenodo.7061868)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/rohitgeddam/FindMyRoomie.svg)](https://GitHub.com/rohitgeddam/FindMyRoomie/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/rohitgeddam/FindMyRoomie.svg)](https://GitHub.com/rohitgeddam/FindMyRoomie/issues?q=is%3Aissue+is%3Aclosed)
![GitHub version](https://img.shields.io/github/v/release/rohitgeddam/FindMyRoomie)

# FindMyRoomie 👯‍♂️

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

   `cd src`

   `python manage.py runserver`
   
Click the link next to "Starting development server at " to view the project

## How to create a new webpage

Read the instructions starting from "Here we create the varied pages and assign the respective HTML files" on this webpage: https://www.geeksforgeeks.org/django-creating-a-multi-page-website/

## After adding another field to Model
Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

   `py manage.py makemigrations`
   
   `py manage.py migrate`

## Populate fake data for testing

```
python manage.py seed_users <number of fake instances>

# creates 10 fake users
python manage.py seed_users 10
```

## Live Server Test Demo
