import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


# Create your tests here.
class ProfileFormTest(LiveServerTestCase):

    def testform(self):
        selenium = webdriver.Chrome(ChromeDriverManager().install())

        selenium.maximize_window()  # For maximizing window
        selenium.implicitly_wait(20)  # gives an implicit wait for 20 seconds

        # Choose your url to visit
        selenium.get('http://127.0.0.1:8000/profile/')

        time.sleep(2)

        # find the elements you need to submit form
        person_name = selenium.find_element(By.ID, "id_name")
        person_bio = selenium.find_element(By.ID, "id_bio")
        person_birth_data = selenium.find_element(By.ID, "id_birthdate")
        person_hometown = selenium.find_element(By.ID, "id_hometown")

        submit = selenium.find_element(By.ID, "submit_button")

        # populate the form with data
        person_name.send_keys("Michelle Obama")
        person_bio.send_keys("Hi! I'm looking for a roomate!")
        person_birth_data.send_keys("03/01/2000")
        person_hometown.send_keys("Chicago, Illinois")

        time.sleep(3)

        # submit form
        submit.send_keys(Keys.RETURN)

        time.sleep(2)

        print(selenium.page_source)

        # check result; page source looks at entire html document
        assert "Michelle Obama" in selenium.page_source

        selenium.close()
