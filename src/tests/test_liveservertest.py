# import time
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys


# class ProfileFormTest(LiveServerTestCase):
#     def test_form(self):
#         selenium = webdriver.Chrome(ChromeDriverManager().install())

#         selenium.maximize_window()  # For maximizing window

#         time.sleep(2)

#         selenium.get("http://127.0.0.1:8000/profile/edit/")

#         time.sleep(30)

#         # find the elements you need to submit form
#         person_name = selenium.find_element(By.ID, "id_name")
#         person_bio = selenium.find_element(By.ID, "id_bio")
#         person_birth_data = selenium.find_element(By.ID, "id_birth_date")
#         person_hometown = selenium.find_element(By.ID, "id_hometown")
#         person_gender = selenium.find_element(By.ID, "id_gender")
#         person_diet = selenium.find_element(By.ID, "id_diet")
#         person_degree = selenium.find_element(By.ID, "id_degree")
#         person_course = selenium.find_element(By.ID, "id_course")
#         person_country = selenium.find_element(By.ID, "id_country")
#         person_p_gender = selenium.find_element(By.ID, "id_preference_gender")
#         person_p_degree = selenium.find_element(By.ID, "id_preference_degree")
#         person_p_diet = selenium.find_element(By.ID, "id_preference_diet")
#         person_p_country = selenium.find_element(
#             By.ID, "id_preference_country"
#         )
#         person_p_course = selenium.find_element(By.ID, "id_preference_course")

#         submit = selenium.find_element(By.ID, "submit_button")

#         time.sleep(5)

#         # populate the form with data
#         person_name.send_keys("Michelle Obama")
#         person_bio.send_keys("Hi! I'm looking for a roommate!")
#         person_birth_data.send_keys("03/01/2000")
#         person_hometown.send_keys("Chicago, Illinois")
#         person_gender.send_keys("Female")
#         person_diet.send_keys("Veg")
#         person_degree.send_keys("PHD")
#         person_course.send_keys("Computer Science")
#         person_country.send_keys("United States of America")
#         person_p_gender.send_keys("Female")
#         person_p_degree.send_keys("PHD")
#         person_p_diet.send_keys("Veg")
#         person_p_country.send_keys("United States of America")
#         person_p_course.send_keys("Computer Science")

#         time.sleep(5)

#         # submit form
#         submit.send_keys(Keys.RETURN)

#         time.sleep(2)

#         print(selenium.page_source)

#         # check result; page source looks at entire html document
#         assert "Michelle Obama" in selenium.page_source

#         selenium.close()
