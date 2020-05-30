# Basic Selenium Drag Drop Operation Automation Using Web Chrome Driver Application in Python 3
# http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
# Using This Tutorial For Reference:: https://www.linkedin.com/learning/using-python-for-automation/basic-browser-interactions?u=2212217
# Packages Required Windows or OS Dependent Chrome Driver & pip install -U selenium (Selenium Package)
# Get Selenium Current stable release: ChromeDriver 81.0.4044.138 From:: https://chromedriver.chromium.org/
# Import Selenium Web Driver From Selenium Package
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# Init Web Driver Chrome
driver = webdriver.Chrome()
# Get The URL TO Browse
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
# Drag & Drop The Capital Field Washington -> United States Field Using Xpath
source_city_washington = driver.find_element_by_xpath('//*[@id="box3"]')
dest_country_usa = driver.find_element_by_xpath('//*[@id="box103"]')
actions = ActionChains(driver)
actions.drag_and_drop(source_city_washington,dest_country_usa).perform()
# Drag & Drop The Capital Field Rome -> Italy Field Using Xpath
source_city_rome = driver.find_element_by_xpath('//*[@id="box6"]')
dest_country_italy = driver.find_element_by_xpath('//*[@id="box106"]')
actions = ActionChains(driver)
actions.drag_and_drop(source_city_rome,dest_country_italy).perform()