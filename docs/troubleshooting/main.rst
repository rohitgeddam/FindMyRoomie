***************
Troubleshooting
***************

* If you come across any error where requirements are not met, run the following command in the project directory:
``pip install -r requirements.txt``

* If you do not make migrations after adding another field to the model, you will face an error, ensure you run the follown\ing commands:
``python manage.py makemigrations``  

``python manage.py migrate``

* If you are facing any lint issues, ensure you have performed the pre-commit hook as mentioned in the quickstart guide.