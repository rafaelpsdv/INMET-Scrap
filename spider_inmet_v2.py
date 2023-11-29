# Coded by Rafael Silva
# E-mail: rafaelps.fis@gmail.com
# 11/24/2023

# Importing libs

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Importing Stations

from stations import stations

# If chrome is closing by itself:
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# Set browser

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

# Set parent link
parentLink = 'https://tempo.inmet.gov.br/TabelaEstacoes/'

# Access each station
for station in stations:
    composedLink = f'{parentLink}{stations[station]}/'
    browser.get(composedLink)
    time.sleep(4)    
    browser.find_element('xpath', '//*[@id="root"]/div[2]/div[2]/div/div/div/span/a').click()
time.sleep(3)
browser.quit()


