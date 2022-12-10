
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys



chromeDriver_path="C:\\Users\\anish\\Downloads\\chromedriver_win32\\chromedriver"
driver = webdriver.Chrome(executable_path=chromeDriver_path)
URL = "https://www.linkedin.com/"
driver.get("https://www.linkedin.com/")
driver.maximize_window()
time.sleep(2)
email=driver.find_element(By.ID,"session_key")
email.click()
email.clear()
email.send_keys("wrong_email@gmail.com")
time.sleep(2)
password=driver.find_element(By.ID,"session_password")
password.click()
password.send_keys("wrong_pass")
signin_button=driver.find_element(By.CLASS_NAME,"sign-in-form__submit-button")
signin_button.click()
print('\n Test case ==> Passed')
time.sleep(3)

#TestCase 2
#Wrong Password
driver.get(URL)
email=driver.find_element(By.ID,"session_key")
email.click()
email.clear()
email.send_keys("correct_email@gmail.com")
time.sleep(5)
password=driver.find_element(By.ID,"session_password")
password.click()
password.send_keys("wrong_pass")
signin_button=driver.find_element(By.CLASS_NAME,"sign-in-form__submit-button")
signin_button.click()
print('\n Test case ==> Passed')
time.sleep(3)

#TestCase 3
#Correct Password Wrong id
driver.get(URL)
driver.maximize_window()
time.sleep(10)
email=driver.find_element(By.ID,"session_key")
email.click()
email.clear()
email.send_keys("wrong_email@gmail.com")
time.sleep(2)
password=driver.find_element(By.ID,"session_password")
password.click()
password.send_keys("correct_pass")
signin_button=driver.find_element(By.CLASS_NAME,"sign-in-form__submit-button")
signin_button.click()
print('\n Test case ==> Passed')
time.sleep(3)

#TestCase 4
#Correct ID and PASSWORD
driver.get(URL)
driver.maximize_window()
time.sleep(3)
email=driver.find_element(By.ID,"session_key")
email.click()
email.clear()
email.send_keys("anishgoyal750@gmail.com")
time.sleep(2)
password=driver.find_element(By.ID,"session_password")
password.click()
password.send_keys("ani912700708")
signin_button=driver.find_element(By.CLASS_NAME,"sign-in-form__submit-button")
signin_button.click()
print('\n Test case ==> Passed')
time.sleep(3)
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

# sign_in_button = driver.find_element_by_link_text("Sign in")
# sign_in_button.click()
# email_field = driver.find_element("username")
# email_field.send_keys("anishgoyal750@gmail.com")
