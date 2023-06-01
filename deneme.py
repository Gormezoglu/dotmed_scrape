# Purpose: Scrape dotmed.com for medical equipment listings

import io
import os
import csv
import time
from datetime import datetime
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException




options = Options()



options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1420,1080')
options.add_argument('--disable-gpu')




#to get latest version of chrome driver into working directory instead of system directory
os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_LOCAL'] = '1'



browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

BASE_URL = "https://www.dotmed.com/webstore/?user=193414&description=0&manufacturer=0&mode=all&sort=&order=&type=parts"
browser.get(BASE_URL)

# Scrape href values from each page
while True:
    time.sleep(3)  # Add a short delay to allow the page to load

    elements = browser.find_elements(By.XPATH, "//*[starts-with(@id, 'listing_')]")

    # Extract the href values from child elements
    for element in elements:
        print("length of elements: ",len(elements))
        listing_text = element.text.split('\n')
        href_value = element.find_element(By.XPATH, ".//a").get_attribute("href")
        print(listing_text,",",href_value)
        #print(listing_text[0].replace('.',''))


    try:
        offset = str(listing_text[0].replace('.',''))
        #print(offset)
        url = f"https://www.dotmed.com/webstore/?user=193414&ajaxShowCats=0&header=-1&pcode=-1&description=0&manufacturer=0&ajaxSearchCats=0&searchPhrase=&mode=all&desc=0&type=parts&order=&sort=&offset={offset}"
        #print(url)       
       # Load the URL
        browser.get(url)
        time.sleep(3)  # Add a short delay to allow the page to load

    except NoSuchElementException:
        print("manuel link doesn't work")
        break

browser.quit()
