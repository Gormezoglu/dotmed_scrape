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

print(browser.page_source)
