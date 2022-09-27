
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
