# Sauce-Demo
Automate the Sauce Demo website

Assignment Objective:
The purpose of this assignment is to help you understand the click and sendKeys actions in automation.

Task 2
Automate the Sauce Demo website
URL: https://www.saucedemo.com/inventory.html

Steps to Automate:
Launch the browser.
Log in to the website.
Add six products to the cart, one after the other.
Log out of the website.
Additionally, can we schedule a 30-minute class today at 8?

New update with my code 
As am rewriting the current code by defining the variable 

Overview

This Selenium script automates the login, product selection, Add product to carts,and logout process on the Sauce Demo website.

Prerequisites

i have you have installed on my system:

Python (>= 3.x)

Google Chrome browser

Chrome WebDriver

Selenium library

Installation

Install Selenium using pip:

pip install selenium

Download and install Chrome WebDriver compatible with your Chrome browser version from Chromedriver.
(WebDriver Managemer) where i don't have to bother if my chrome webdriver is compatible with my browser

Script Functionality

Opens the Sauce Demo login page.

Logs in using predefined credentials.

Adds specific products to the cart.

Logs out and closes the browser.

Usage

Save the script as sauce_demo_automation.py.

Run the script using:

python sauce_demo_automation.py

Customization

Modify USERNAME and PASSWORD variables to use different credentials.

Adjust WAIT_TIME to optimize performance.

Add or remove product IDs from the PRODUCT list to customize the cart items.

Notes

This script uses time.sleep(WAIT_TIME), which may be replaced with Selenium's explicit waits for better efficiency.

I have checked if the website is accessible before running the script.

