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

   `cd Roomies`

   `python manage.py runserver`
   
Click the link next to "Starting development server at " to view the project

## How to create a new webpage

Read the instructions starting from "Here we create the varied pages and assign the respective HTML files" on this webpage: https://www.geeksforgeeks.org/django-creating-a-multi-page-website/

## Location of important files
CSS is in `Roomies/static/style`

Images are in `Roomies/static/images`


## How to contribute 
1) Pull from develop branch.
2) Create a feature branch with name feature_<feature_name>.
3) Once you are done working on your feature, merge develope into your feature branch.
4) Push yout branch to github, and open a a PR to develop branch.
5) Add reviewers while your create a PR, and wait for your feature to get merged. 
6) Start working on a new feature.
