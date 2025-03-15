import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the login page
driver.get("https://www.saucedemo.com")  # Fixed the URL to the login page
time.sleep(5)

# Log in
driver.find_element(By.ID, "user-name").send_keys("problem_user")  # Enter username
time.sleep(5)
driver.find_element(By.ID, "password").send_keys("secret_sauce")  # Enter password
time.sleep(5)
driver.find_element(By.ID, "login-button").click()  # Click Log in button
time.sleep(5)

# Verify login success by checking the inventory page
if "inventory.html" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed!")

# Product Page - Adding items to the cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()  # Add first item to cart
time.sleep(5)

driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()  # Add second item to cart
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()  # Add third item to cart
time.sleep(5)

driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()  # Add fourth item to cart
time.sleep(5)

driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()  # Add fifth item to cart
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
time.sleep(50)

# Click hamburger menu and logout
driver.find_element(By.ID, "react-burger-menu-btn").click()  # Click hamburger menu
time.sleep(5)

driver.find_element(By.ID, "logout_sidebar_link").click()  # Click log out button
time.sleep(5)

# Close the browser
driver.quit()
