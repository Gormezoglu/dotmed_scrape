# Purpose: Scrape dotmed.com for medical equipment listings


import io
import os
import csv
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import time
from datetime import datetime


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

browser.get('https://www.dotmed.com/webstore/?user=193414&description=-1&manufacturer=-1&mode=all&sort=&order=&type=parts')

# Find the listings on the page
listings = browser.find_elements(By.CLASS_NAME, "ListingContainer")

print(listings)

# Process the listings
for listing in listings:
    title = listing.find_element(By.CLASS_NAME, "row listing-list ml-0 mr-0 mt-3 mb-3 listings-d").text.strip()
    price = listing.find_element(By.CLASS_NAME, "ListingPrice").text.strip()
    description = listing.find_element(By.CLASS_NAME, "ListingDescription").text.strip()

    print("Title:", title)
    print("Price:", price)
    print("Description:", description)
    print("----------------------")

# listing returns blank. edit class name and try again
