# Basic Selenium Automation Using Web Chrome Driver Application in Python 3
# Using This Tutorial For Reference:: https://www.linkedin.com/learning/using-python-for-automation/basic-browser-interactions?u=2212217
# Packages Required Windows or OS Dependent Chrome Driver & pip install -U selenium (Selenium Package)
# Get Selenium Current stable release: ChromeDriver 81.0.4044.138 From:: https://chromedriver.chromium.org/
# Interacting Basic Demo 1st Form Field Message & Summation Field Using XPath & Css Selector
# Using Explicit & Implicit Wait For The Web Pages That Loads AJAX OR NAGGING SCREENS
# Import Selenium Web Driver From Selenium Package
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Init Web Driver Chrome
driver = webdriver.Chrome()
# Get The URL TO Browse
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
# Wait The Explicit Wait 5s
wait = WebDriverWait(driver,5)
# Check For Nagging Screen To Appear and Close it By Using Wait & Expected Condition Check
nagging_screen = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="at-cv-lightbox-button-holder"]/a[2]')))
# Click The Close Bttn
nagging_screen.click()
# Find The Message Field Using Xpath
input_message_field = driver.find_element_by_xpath('//*[@id="user-message"]')
# Input The Message in This Field
input_message_field.send_keys('Hello Selenium Automation 2')
# Get Button Field For Click using Xpath
input_message_field_bttn = driver.find_element_by_xpath('//*[@id="get-input"]/button')
# Click the input_message_field_bttn
input_message_field_bttn.click()
# Getting Sum Input Field 1 Css Selector
input_sum_1 = driver.find_element_by_css_selector('#sum1')
# Now Input Sum Field 1 Css Selector
input_sum_1.send_keys('12')
# Getting Sum Input Field 2
input_sum_2 = driver.find_element_by_css_selector('#sum2')
# Now Input Sum Field 2 Css Selector
input_sum_2.send_keys('20')
# Getting Sum Bttn Field Css Selector.
input_sum_bttn = driver.find_element_by_css_selector('#gettotal > button')
# Now Click Bttn Field
input_sum_bttn.click()