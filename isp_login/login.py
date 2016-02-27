#!/usr/bin/env python2.7
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox() # Define browser as Firefox
driver.set_window_size(600,600) # Set size of your browser window.
driver.get("YOUR_ISP_URL") # Replace this with the url of your own ISP's login page.
time.sleep(10) # Wait for 10 seconds after loading the ISP page.


try:
    login_attempt = driver.find_element_by_xpath("//*['Please log on to use the Broadband Service.']") # It can be any Other Custom Message. So replace it. Example: 'Login to your profile.''
    username = driver.find_element_by_id("inputUsername") # It's the HTML Form Input ID of your Username. Replace it.
    password = driver.find_element_by_id("inputPassword") # It's the HTML Form Input ID of your Password. Replace it too.
    username.send_keys("YOUR_USERNAME_HERE") # Replace this with your own Username.
    password.send_keys("YOUR_PASSWORD_HERE") # Replace this with your own Password.
    login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
    login_attempt.submit()
    assert "You are logged in successfully." in driver.page_source # Asserts that you have logged in successfully and prints a custom message.
    print("You're successfully logged in.")
    time.sleep(5)
    driver.close() # Closes the browser window.

except NoSuchElementException: # If you're already logged in, without showing an error, it shows you a custom message.
    print("Oh, you're already logged in.")
    time.sleep(5)
    driver.close()
