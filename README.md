[![Test](https://github.com/rohitgeddam/FindMyRoomie/actions/workflows/Unit_Tests.yml/badge.svg)](https://github.com/rohitgeddam/FindMyRoomie/actions/workflows/Unit_Tests.yml)
[![codecov](https://codecov.io/gh/rohitgeddam/FindMyRoomie/branch/main/graph/badge.svg?token=PCOHJETYCD)](https://codecov.io/gh/rohitgeddam/FindMyRoomie)
[![Test](https://github.com/rohitgeddam/FindMyRoomie/actions/workflows/Linting.yml/badge.svg)](https://github.com/rohitgeddam/FinMyRoomie/actions/workflows/Linting.yml)
![CodeQL](https://github.com/rohitgeddam/FindMyRoomie/workflows/CodeQL/badge.svg)
[![code_size](https://img.shields.io/github/languages/code-size/rohitgeddam/CSC510_PROJECT1)](https://github.com/rohitgeddam/CSC510_PROJECT1) 
[![repo_size](https://img.shields.io/github/repo-size/rohitgeddam/CSC510_PROJECT1)](https://github.com/rohitgeddam/CSC510_PROJECT1)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7155519.svg)](https://doi.org/10.5281/zenodo.7155519)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/rohitgeddam/FindMyRoomie.svg)](https://GitHub.com/rohitgeddam/FindMyRoomie/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/rohitgeddam/FindMyRoomie.svg)](https://GitHub.com/rohitgeddam/FindMyRoomie/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub version](https://img.shields.io/github/v/release/rohitgeddam/FindMyRoomie)](https://github.com/rohitgeddam/FindMyRoomie/releases)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# FindMyRoomie
<p align = "justify">
'FindMyRoomie' is a Web Application that provides a platform for lonely wolves (NC State students) to find roommates of their preference. The stakes are high when it comes to finding your best roommate because this relationship starts with a living relationship :sweat_smile:. We understand how stressful this can be, especially if you are moving to a new city or country. FindMyRoomie is a one-stop solution to your roommate finding needs. Our software has functionalities that allow you to filter and choose your ideal roommate. But if that is too much work for you, we also provide roommate suggestions based on your preferences! Any NC State student could sign up with their NC State Email address from any corner of the world on our website and begin searching for roommates. 
</p>

<p align = "center">
<img width = "400", src = "https://user-images.githubusercontent.com/52373569/194727868-201a036a-c400-46c4-b359-98777a92ce86.gif">
</p>

<p align = "justify">
The software is free for use by anyone, and we also welcome any contributions to improve our software (Please read our [CONTRIBUTING.md](https://github.com/rohitgeddam/FindMyRoomie/blob/main/CONTRIBUTING.md) file for more details). If you would like to cite our repository, please check our [CITATION.cff](https://github.com/rohitgeddam/FindMyRoomie/blob/main/CITATION.cff) file.
</p>

## Features of the software

#### 1. SignUp: 

<p align = "center">
<img width = "600" src = "https://user-images.githubusercontent.com/52373569/194731737-93009a6e-141a-4bc8-8ba4-cc898f504186.png">
</p>

  Allows new users to register to our roommate finding portal. New users could register using their NCSU Email ID.

#### 2. SignIn: 

<p align = "center">
<img width = "600" src = "https://user-images.githubusercontent.com/52373569/194731814-4aa13d05-3c17-4723-a444-e69d02d949a3.png">
</p>

  Allows existing users to LogIn to our website using their credentials.

#### 3. Homepage:
<p align = "center">
<img width = "600" src ="https://user-images.githubusercontent.com/52373569/194731856-0130e163-cea8-4897-941c-530f5bf9dec3.png">

  A page with happy Mr. and Mrs. Wolf enjoying each other's company in the background, just like you and your roommates would be :heart_on_fire:. 

#### 4. My Profile: 
<p align = "justify">
Allows you to introduce whom you are to your future roommate! You are given the opportunity to tell others a little bit about yourself and your preferences. The "Visibility" checkbox in your profile allows you to choose whether you want to be visible to others. If you are looking for roommates, you can toggle it on, and if you have found one (Congratulations :partying_face: :partying_face:), you can toggle it off. It's that easy!
</p>

 #### 5. Find people:
 
 Lists the people looking for roommates just like you. Our "Wolf Filter" lets you filter candidates based on your preferences :wolf:. Be choosy!!	

 #### 6. My room:

  Lists your roommates (feature not available yet) and provides roommate suggestions based on your preferences. The similarity scores with other roommate seekers are calculated based on the Manhattan Distance, and the people with the top scores are shown as suggestions. 
 
#### The website flow is depicted in the below video:


## Set up the project on your local machine

#### 1. Clone the repository:  

   `git clone https://github.com/rohitgeddam/FindMyRoomie.git`

#### 2. Setup the virtual environment:  
    
    `python -m venv venv`

#### 3. Activate the virtual environment:  

    * On Mac/Linux:    
    
      `source venv/bin/activate`
      
    * On Windows:    
    
      `venv\Scripts\activate`
   
#### 3. Install required modules and libraries:  

    `pip install -r requirements.txt`

#### 4. Run the application:  
   
   ```
   cd src 
   python manage.py migrate
   python manage.py runserver
   ```
  
## After adding another field to Model
Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

## Populate fake data for testing

```
python manage.py seed_users <number of fake instances>

# creates ten fake users
python manage.py seed_users 10
```

## Automatic tools - GitHub Actions
 
We use GitHub actions to automate tasks of linting, code coverage, build, tests, and security checks. The codes that perform these actions are stored as `.yml` files in the `.github/workflows` directory. The GitHub actions are triggered whenever something is pushed (or pulled) into the remote repository. The results of these automated tasks are shown as badges at the top of this README.md file. 

### Unit tests:

`Unit_Tests.yml` performs automated testing. Each time a commit occurs in the remote repository, tests are run automatically on the entire codebase. More details about the tests could be found in [Test README](https://github.com/rohitgeddam/FindMyRoomie/tree/main/src/tests#readme).

### Code Coverage: 

Code Coverage is an important metric that allows us to understand how much of the codebase is tested. `Code_Cov.yml` performs this task. For more information about Code Coverage, please visit this [link](https://www.atlassian.com/continuous-delivery/software-testing/code-coverage). 

### Flake8 - Code Linting:

We are using Flake8 for linting and syntax checking, and it is performed by `Linting.yml`. For more information about Flake8, please visit this [link](https://medium.com/python-pandemonium/what-is-flake8-and-why-we-should-use-it-b89bd78073f2).
Use flake8 before you push code to GitHub. </br>
Config file present in `setup.cfg`.

```
flake8 <directory>
```

### Black - Code Formatter

We are using the Black code formatter to format our code before pushing it to GitHub. For more information about Black, please visit this [link](https://black.readthedocs.io/en/stable/).

Run the line below everytime you push to GitHub.</br>
Config file present in `pyproject.toml`
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
  
### Pre Commit Hooks for Black Code formatting and Flake8 Linting
* run  `pre-commit install`
* Now everytime you commit, Black and Flake8 will run automatically and will not allow you to push if the code standards are not met.
<img width="694" alt="Screenshot 2022-10-07 at 11 35 40 AM" src="https://user-images.githubusercontent.com/48797475/194592802-e7d7c951-9694-4260-b537-fc017a5fd06c.png">

### CodeQL

`CodeQL.yml` performs automated security checks on the codebase and scans it for any vulnerabilities and bugs. For more information about CodeQL, please visit this [link](https://codeql.github.com/docs/codeql-overview/about-codeql/). 
  
## Privacy Notice

#### 1. What personal details of yours would you be sharing with us and why?
<p align = "justify">
To aid you in your roommate search, to help others find you, and also to provide you with relevant roommate suggestions, you will be asked to share your "Name", "Email", "Date of Birth", "Gender", "Diet", "Hometown", "Degree and Course", "Country of Origin". You are free to include anything in your bio (which could include your Instagram ID and other social media handles). 

#### 2. Will we be storing your details, and how will we use them?

Yes, we will be storing them in our database. We will ONLY use this to match you with potential roommates and improve our software. 

#### 3. Will we share it with any third-party institutions?

NO. Your data is safe with us :slightly_smiling_face:. We will not share/lend/rent your data to any outside institutions/personnel.

#### 4. How long will you store my data?

We retain your information as long as needed to provide you with our services.

#### 5. How to remove my data from the website?

Our current release does not provide you with a mechanism to remove your data directly from our website. You are always free to turn off your visibility. If you still feel the need to remove your data from our website, kindly email one of the contributors from your registered Email ID, and we will take care of the rest!
</p>

## Technology Used
-   `Python 3.7+`
-   `Django 4.1.2`
-   `HTML5`
-   `CSS3`
-   `BootStrap v5.2`

## Future features/work:
1. Include the Apartment in the profile section. Along with the budget of each person.
2. Include features of MyRoom.
3. Add leasing/subleasing apartments.
4. Chat room to chat with other users. 

## Contact us:
Rohit Geddam: sgeddam2@ncsu.edu </br>
Arun Kumar Ramesh - arames25@ncsu.edu </br> 
Kiron Jayesh - kjayesh@ncsu.edu </br>
Sai Krishna Teja Varma - smanthe@ncsu.edu </br>
Shandler Mason - samason4@ncsu.edu </br>

## License:
Distributed under the MIT License. See `LICENSE` for more information

#


<p align = "center">
<img width = "450" src = "https://user-images.githubusercontent.com/52373569/194727890-48c53f9d-f351-433e-82bf-df33d7945b25.gif">
</p>
=======

## Contact Us:
* Email: ncsu.findmyroomie@gmail.com
* Twitter: [Twitter Profile](https://twitter.com/findmyroomie_nc)
* Chat/Discuss: [Github Discussions](https://github.com/rohitgeddam/FindMyRoomie/discussions)

