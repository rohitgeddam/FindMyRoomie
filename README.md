[![Test](https://github.com/rohitgeddam/FindMyRoomie/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/rohitgeddam/FinMyRoomie/actions/workflows/unit_tests.yml)
[![codecov](https://codecov.io/gh/rohitgeddam/FindMyRoomie/branch/main/graph/badge.svg?token=PCOHJETYCD)](https://codecov.io/gh/rohitgeddam/FindMyRoomie)
[![Test](https://github.com/rohitgeddam/FindMyRoomie/actions/workflows/linting.yml/badge.svg)](https://github.com/rohitgeddam/FinMyRoomie/actions/workflows/linting.yml)
![CodeQL](https://github.com/rohitgeddam/FindMyRoomie/workflows/CodeQL/badge.svg)
[![code_size](https://img.shields.io/github/languages/code-size/rohitgeddam/CSC510_PROJECT1)](https://github.com/rohitgeddam/CSC510_PROJECT1) 
[![repo_size](https://img.shields.io/github/repo-size/rohitgeddam/CSC510_PROJECT1)](https://github.com/rohitgeddam/CSC510_PROJECT1)</br>
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7155519.svg)](https://doi.org/10.5281/zenodo.7155519)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/rohitgeddam/FindMyRoomie.svg)](https://GitHub.com/rohitgeddam/FindMyRoomie/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/rohitgeddam/FindMyRoomie.svg)](https://GitHub.com/rohitgeddam/FindMyRoomie/issues?q=is%3Aissue+is%3Aclosed)
![GitHub version](https://img.shields.io/github/v/release/rohitgeddam/FindMyRoomie)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# FindMyRoomie 👯‍♂️

FindMyRoomie is a Web Application that provides a platform for NC State students to find roomates of their preference. The software has functionalities that allows you to filter and choose your ideal roommate. But if that is too much work for you, we also provide roommate suggestions based on your preferences! The software is free for use to anyone, and we also welcome any contributions to improve our software application (Please read our [Contributions.md](https://github.com/rohitgeddam/FindMyRoomie/blob/main/CONTRIBUTING.md) file for more details). If you would like to cite our repository, please check our [Citations.cff](https://github.com/rohitgeddam/FindMyRoomie/blob/main/CITATION.cff) file. 

![roommate-rachel](https://user-images.githubusercontent.com/52373569/194727868-201a036a-c400-46c4-b359-98777a92ce86.gif)


Check this website to write about high level design in README.md: https://ipwithease.com/what-is-a-high-level-design-hld/

The components of the application include:
1. SignUp - Allows new users to register to our roommate finding portal.
2. LogIn - Allows existing users to continue their roommate search.
3. Homepage - A page that has a happy Mr. and Mrs. Wolf enjoying each others company in the background, just like you and your roommates would be. 
4. My Profile - Allows you to express a little about who you are, and what you want from your roommate.
5. Find people - Lists the people who are looking for roommates just like you. The "Wolf Filter" lets you to filter candidates based on your preferences.
6. My room - Lists your roommates (feature not available yet), and also provides suggestions based on your preferences.  

#### (Write about problem statement and aim. Provide a clear, high-level overview of the software. Describe the type of user who should use your software. make note that the software is available for free).

## Software commands and functions

## Features of the software

Visibility - 
Roomate suggestion - Similarity score
(Manhattan distance - similarity score)

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

## Automatic tools - GitHub Actions

### Unit tests

### Code Coverage

### Flake8 - Code Linting

We are using Flake8 for linting and syntax checking.
Use flake8 before you push code to github.
config file present in `setup.cfg`

```
flake8 <directory>
```

### Black - Code Formatter

We are using Black code formatter to format our code before pushing to github.
Run the line below everytime you push to github.
config file present in `pyproject.toml`
```
black --line-length 120 <filename>
```

If you prefer using Black in VSCode, you can add the below settings in your vscode settings
```
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length", "120"],
    "python.linting.enabled": true
}
```

## Privacy Notice

1. What personal details of yours would you be sharing with us and why?

To aid you in your roommate search, to help others find you and also to provide you relevant roommate suggestions, you will be asked to share your "Name", "Email", "Date of Birth", "Gender", "Diet", "Hometown", "Degree and Course", "Country of Origin". You are free to include anything in your bio (which could include your instagram ID and other social media handles). 

2. Will we be storing your details and if so how would we use them?

Yes, we will be storing them in our database. This will ONLY be used by us to match you with potential roommates and to improve our software. 

3. Will we share it with any third-party instituitons?

NO. Your data is safe with us and we will not be sharing/lending/renting it with any outside instituitons/personnel.

4. How long will you store my data?

We retain your information as long as needed to provide you with our services.

5. How to remove my data from the website?

Our current release does not provide you a mechanism to remove your data from our website. You are always free to turn off your visibility. If you still feel the need to remove your data from our website, kindly email one of the contributors from your registered Email ID, and we will take care of the rest!

## Future features/work:
1. Include Apartment in the profile section. Along with the budget of each person.
2. Include features of MyRoom.

## Technology Used
-   `Python 3.7+`
-   `Django 4.1.2`
-   `HTML5`
-   `CSS3`

## Contact us:
Rohit Geddam - rgeddam@ncsu.edu </br>
Arun Kumar Ramesh - arames25@ncsu.edu </br> 
Kiron Jayesh - kjayesh@ncsu.edu </br>
Sai Krishna Teja Varma - smanthe@ncsu.edu </br>
Shandler Mason - samason4@ncsu.edu </br>

## License:
Distibuted under the MIT License. See `LICENSE` for more information

![jim-parsons-sheldon-cooper](https://user-images.githubusercontent.com/52373569/194727890-48c53f9d-f351-433e-82bf-df33d7945b25.gif)
