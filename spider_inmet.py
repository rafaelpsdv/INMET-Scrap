# Coded by Rafael Silva
# E-mail: rafaelps.fis@gmail.com
# 11/27/2023

# Importing libs

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Importing Stations file

from stations import stations

# If chrome is closing by itself:
chrome_options = Options()
# chrome_options.add_argument('--headless') -- NOT WORKING
chrome_options.add_experimental_option("detach", True)


# Set browser
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

time.sleep(3)

# Set parent link
parentLink = 'https://tempo.inmet.gov.br/TabelaEstacoes/'

# Collecting data

for station in stations:
    composedLink = f'{parentLink}{stations[station]}/'
    browser.get(composedLink)
    time.sleep(4)
    
    data = browser.find_elements(By.XPATH, '//tbody/tr/td[1]')
    hora = browser.find_elements(By.XPATH, '//tbody/tr/td[2]')
    temp_inst = browser.find_elements(By.XPATH, '//tbody/tr/td[3]')
    temp_max = browser.find_elements(By.XPATH, '//tbody/tr/td[4]')
    temp_min = browser.find_elements(By.XPATH, '//tbody/tr/td[5]')
    umidade_inst = browser.find_elements(By.XPATH, '//tbody/tr/td[6]')
    umidade_max = browser.find_elements(By.XPATH, '//tbody/tr/td[7]')
    umidade_min = browser.find_elements(By.XPATH, '//tbody/tr/td[8]')
    pto_orvalho_inst = browser.find_elements(By.XPATH, '//tbody/tr/td[9]')
    pto_orvalho_max = browser.find_elements(By.XPATH, '//tbody/tr/td[10]')
    pto_orvalho_min = browser.find_elements(By.XPATH, '//tbody/tr/td[11]')
    pressao_inst = browser.find_elements(By.XPATH, '//tbody/tr/td[12]')
    pressao_max = browser.find_elements(By.XPATH, '//tbody/tr/td[13]')
    pressao_min = browser.find_elements(By.XPATH, '//tbody/tr/td[14]')
    vento_vel = browser.find_elements(By.XPATH, '//tbody/tr/td[15]')
    vento_dir = browser.find_elements(By.XPATH, '//tbody/tr/td[16]')
    vento_raj = browser.find_elements(By.XPATH, '//tbody/tr/td[17]')
    radiacao = browser.find_elements(By.XPATH, '//tbody/tr/td[18]')
    chuva = browser.find_elements(By.XPATH, '//tbody/tr/td[19]')

    datas = []
    for i in range(len(hora)):
        temporary_data = {'hora':hora[i].text,
                        'temp_inst':temp_inst[i].text,
                        'temp_max':temp_max[i].text,
                        'temp_min':temp_min[i].text,
                        'umidade_inst':umidade_inst[i].text,
                        'umidade_max':umidade_max[i].text,
                        'umidade_min':umidade_min[i].text,
                        'pto_orvalho_inst':pto_orvalho_inst[i].text,
                        'pto_orvalho_max':pto_orvalho_max[i].text,
                        'pto_orvalho_min':pto_orvalho_min[i].text,
                        'pressao_inst':pressao_inst[i].text,
                        'pressao_max':pressao_max[i].text,
                        'pressao_min':pressao_min[i].text,
                        'vento_vel':vento_vel[i].text,
                        'vento_dir':vento_dir[i].text,
                        'vento_raj':vento_raj[i].text,
                        'radiacao':radiacao[i].text,
                        'chuva':chuva[i].text
                        }
        datas.append(temporary_data)
    pd.DataFrame(datas).to_csv(f'tabela-{station}.csv')

browser.quit()

