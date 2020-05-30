# Basic Google Translate English Good Morning To Hindi (Shubh Prabhaat) in Python 3
# Packages Required Windows or OS Dependent Chrome Driver & pip install -U selenium (Selenium Package)
# Get Selenium Current stable release: ChromeDriver 81.0.4044.138 From:: https://chromedriver.chromium.org/
# Import Selenium Web Driver From Selenium Package
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Init Web Driver Chrome
driver = webdriver.Chrome()
# Get The URL TO Browse
driver.get('https://translate.google.com/')
# Wait The Explicit Wait 5s
wait = WebDriverWait(driver,5)
# Click Got It Nagging Popup
GotItNaggingPopup = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[1]/div/div[3]/div/div'))).click()
# Check Select DropDown Arrow For From Language English it By Using Wait & Expected Condition Check
Select_TranslateFromLanguage = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]')))
# Click Drop Down Arrow Button
Select_TranslateFromLanguage.click()
# Find The English Language From The Drop Menu List
select_english_language = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[2]/div/div[3]/div[22]/div[2]')
# Select English
select_english_language.click()
# Get The Translate From (Language Text Area Field)
input_translate_text = driver.find_element_by_xpath('//*[@id="source"]')
# Input The Text
input_translate_text.send_keys('Good Morning')
# Check Select DropDown Arrow For To Language Hindi it By Using Wait & Expected Condition Check
Select_TranslateToLanguage = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[3]')))
# Click The Bttn
Select_TranslateToLanguage.click()
# Select The Language Hindi in the List
select_hindi_language = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div/div[2]/div[2]/div[2]/div/div[2]/div[39]/div[2]')
# Click The Hindi
select_hindi_language.click()
# Listen Translated Word
listen_translation = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[4]/div[5]/div'))).click()