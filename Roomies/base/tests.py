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
        selenium.implicitly_wait(10)  # gives an implicit wait for 20 seconds

        # Choose your url to visit
        selenium.get('http://127.0.0.1:8000/')

        # find the elements you need to submit form
        person_name = selenium.find_element(By.ID, "id_name")
        person_age = selenium.find_element(By.ID, "id_age")
        person_hometown = selenium.find_element(By.ID, "id_hometown")

        submit = selenium.find_element(By.ID, "submit_button")

        # populate the form with data
        person_name.send_keys('Michelle Obama')
        person_age.send_keys('58')
        person_hometown.send_keys('Chicago, Illinois')

        # submit form
        submit.send_keys(Keys.RETURN)

        # check result; page source looks at entire html document
        # assert 'Michelle Obama' in selenium.page_source
