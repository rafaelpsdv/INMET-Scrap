# INMET-Scrap
![Static Badge](https://img.shields.io/badge/LICENSE-MIT-blue) ![Static Badge](https://img.shields.io/badge/Status-In%20development-yellow)

## About this project
The objective of this project is to collect real-time meteorological data from the website of the National Institute of Meteorology of Brazil (INMET) in real time.

## Tecnologies and requeriments
* `Conda 23.7.4`
* `Selenium`
* `Selenium WebDriver`
* `Pandas`

## Related links

* [INMET Portal](https://portal.inmet.gov.br/)
* [INMET's Catalogue of Automatic Stations](https://portal.inmet.gov.br/paginas/catalogoaut)
* [INMET's Catalogue of Conventional Stations](https://portal.inmet.gov.br/paginas/catalogoman)

## About INMET real-time data
The INMET provides on its portal several types of data in many differents modes. The real-time data is updated hourly and when you access you can see this data in a HTML table by station.
The problem on the data collect is that there is a JS script that generate these tables.
As the tables is a dynamic generated, I can't use Pandas or BeautifulSoup4 for extract this data.

**The solution**: Collect data after the JS script run.

### How does this program work?
Basically, his program follow this steps:
1. Access a specific station table.
2. Wait for JS script run.
3. Collect the data from the HTML table.
4. Transform this data in a Data Frame.
5. Export to CSV.
6. Loop for the chosen stations.

## Configuring the program
### Setting the stations:
To set which stations you want do download data, verify the file `stations.py`.
I configured the stations of Mato Grosso do Sul, but you can view the station codes on the Related Links section in this README.

Once you have configured the stations you can select datas that you want to download.

In the file `spider-inmet.py`, in the section "Collecting data" you can comment the lines of the column names that you don't want to download.

Example: 
```
data = browser.find_elements(By.XPATH, '//tbody/tr/td[1]')
hora = browser.find_elements(By.XPATH, '//tbody/tr/td[2]')
# temp_inst = browser.find_elements(By.XPATH, '//tbody/tr/td[3]')
temp_max = browser.find_elements(By.XPATH, '//tbody/tr/td[4]')
temp_min = browser.find_elements(By.XPATH, '//tbody/tr/td[5]')
```
Doing this, the data from collumn Instantaneous Temperature will be not collected



