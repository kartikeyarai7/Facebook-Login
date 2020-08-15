from selenium import webdriver
from selenium.webdriver.common.keys import Keys

for i in range(0,5):
  driver = webdriver.Chrome('./chromedriver')
  driver.get('https://www.facebook.com/')
  email = driver.find_element_by_id("email")
  email.clear()
  email.send_keys("Your email address here")
  password = driver.find_element_by_id("pass")
  password.send_keys("Your password here")
  login = driver.find_element_by_id("u_0_b")
  login.send_keys("TO SUBMIT")
  login.submit()
#   print(driver)
