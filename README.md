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

FindMyRoomie is a Web Application that provides a platform for NC State students to find roommates of their preference. The stakes are high when it comes to finding your best roommate because this relationship starts with a living relationship :sweat_smile:  We understand how stressful this can be. FindMyRoomie is a one-stop solution to your roommate finding needs. Our software has functionalities that allow you to filter and choose your ideal roommate. But if that is too much work for you, we also provide roommate suggestions based on your preferences! Any NC State student could sign up with their NC State Email ID from any corner of the world on our website and begin searching for roommates. 

<p align = "center">
<img width = "400", src = "https://user-images.githubusercontent.com/52373569/194727868-201a036a-c400-46c4-b359-98777a92ce86.gif">
</p>

The software is free for use to anyone, and we also welcome any contributions to improve our software (Please read our [CONTRIBUTING.md](https://github.com/rohitgeddam/FindMyRoomie/blob/main/CONTRIBUTING.md) file for more details). If you would like to cite our repository, please check our [CITATION.cff](https://github.com/rohitgeddam/FindMyRoomie/blob/main/CITATION.cff) file. 

#### (Write about problem statement and aim. Provide a clear, high-level overview of the software. Describe the type of user who should use your software. make note that the software is available for free).

## Software commands and functions

## Features of the software

Pages: 

1. SignUp: 

<p align = "center">
<img width = "600" src = "https://user-images.githubusercontent.com/52373569/194731737-93009a6e-141a-4bc8-8ba4-cc898f504186.png">
</p>

  Allows new users to register to our roommate finding portal. New users could register using their NCSU Email ID.

2. SignIn: 

<p align = "center">
<img width = "600" src = "https://user-images.githubusercontent.com/52373569/194731814-4aa13d05-3c17-4723-a444-e69d02d949a3.png">
</p>

  Allows existing users to LogIn to our website using their credentials.

3. Homepage:
<p align = "center">
<img width = "600" src ="https://user-images.githubusercontent.com/52373569/194731856-0130e163-cea8-4897-941c-530f5bf9dec3.png">

  A page with a happy Mr. and Mrs. Wolf enjoying each other's company in the background, just like you and your roommates would be :heart_on_fire: 

4. My Profile: 

Allows you to introduce whom you are to your future roommate! You are given the opportunity to tell others a little bit about yourself and your preferences. The "Visibility" checkbox in your profile allows you to choose whether you want to be visible to others. If you are looking for roommates, you can toggle it on, and if you have found one (Congratulations :partying_face: :partying_face:), you can toggle it off. It's that easy!

 5. Find people:
 Lists the people looking for roommates just like you. Our "Wolf Filter" lets you filter candidates based on your preferences :wolf:	

 6. My room:
 Lists your roommates (feature not available yet) and provides roommate suggestions based on your preferences. The similarity scores with other roommate seekers are calculated based on the Manhattan Distance, and the people with the top scores are shown as suggestions. 
   

## How to setup the project on your local machine?
1. Download a free Python IDE online, such as PyCharm, Visual Studio Code, Spyder, etc.

2. In the IDE terminal, copy and paste the command: 

   `git clone https://github.com/rohitgeddam/CSC510_PROJECT1.git`

3. To setup the virtual environment

   `python -m venv venv`

    * On Mac/Linux
    
      `source venv/bin/activate`
    * On Windows
    
      `venv\Scripts\activate`
   
   (If you get an error at this step, continue on.)
   
   `pip install -r requirements.txt`

   If you get an error, do `pip install django`. 
   
   If you get this message "ModuleNotFoundError: No module named 'crispy_forms'" enter the command `pip install django-crispy-forms`

4. To run the virtual environment

   Type into the terminal:
   
   ```
   cd src 
   python manage.py runserver
   ```
   
Click the link next to "Starting development server at " to view the project.

## How to create a new webpage

Read the instructions starting from "Here we create the varied pages and assign the respective HTML files" on this webpage: https://www.geeksforgeeks.org/django-creating-a-multi-page-website/

## After adding another field to Model
Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

   ```
   py manage.py makemigrations
   py manage.py migrate
   ```

## Populate fake data for testing

```
python manage.py seed_users <number of fake instances>

# creates ten fake users
python manage.py seed_users 10
```

## Automatic tools - GitHub Actions

### Unit tests:

### Code Coverage: 

### Flake8 - Code Linting:

We are using Flake8 for linting and syntax checking.
Use flake8 before you push code to GitHub.
config file present in `setup.cfg`

```
flake8 <directory>
```

### Black - Code Formatter

We are using the Black code formatter to format our code before pushing it to GitHub.
Run the line below everytime you push to GitHub.
config file present in `pyproject.toml`
```
black --line-length 120 <filename>
```

If you prefer using Black in VSCode, you can add the below settings in your vscode settings:

```
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length", "120"],
    "python.linting.enabled": true
}
```

## Privacy Notice

#### 1. What personal details of yours would you be sharing with us and why?

To aid you in your roommate search, to help others find you, and also to provide you with relevant roommate suggestions, you will be asked to share your "Name", "Email", "Date of Birth", "Gender", "Diet", "Hometown", "Degree and Course", "Country of Origin". You are free to include anything in your bio (which could include your Instagram ID and other social media handles). 

#### 2. Will we be storing your details, and how will we use them?

Yes, we will be storing them in our database. We will ONLY use this to match you with potential roommates and improve our software. 

#### 3. Will we share it with any third-party institutions?

NO. Your data is safe with us, and we will not be sharing/lending/renting it with any outside institutions/personnel.

#### 4. How long will you store my data?

We retain your information as long as needed to provide you with our services.

#### 5. How to remove my data from the website?

Our current release does not provide you with a mechanism to remove your data directly from our website. You are always free to turn off your visibility. If you still feel the need to remove your data from our website, kindly email one of the contributors from your registered Email ID, and we will take care of the rest!

## Technology Used
-   `Python 3.7+`
-   `Django 4.1.2`
-   `HTML5`
-   `CSS3`

## Future features/work:
1. Include the Apartment in the profile section. Along with the budget of each person.
2. Include features of MyRoom.
3. Add leasing/subleasing apartments.
4. Chat room to chat with other users. 

## Contact us:
Rohit Geddam - rgeddam@ncsu.edu </br>
Arun Kumar Ramesh - arames25@ncsu.edu </br> 
Kiron Jayesh - kjayesh@ncsu.edu </br>
Sai Krishna Teja Varma - smanthe@ncsu.edu </br>
Shandler Mason - samason4@ncsu.edu </br>

## License:
Distributed under the MIT License. See `LICENSE` for more information

-----

<p align = "center">
<img width = "450" src = "https://user-images.githubusercontent.com/52373569/194727890-48c53f9d-f351-433e-82bf-df33d7945b25.gif">
</p>
