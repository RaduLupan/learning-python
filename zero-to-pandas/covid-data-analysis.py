'''
This notebook shows some examples of analyzing tabular data with Pandas.
The source CSV is Our World in Data Covid data. 
'''

from urllib.request import urlretrieve
import os

owid_covid_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

# Create the data folder under current directory.
os.makedirs('./data', exist_ok=True)

# Download the covid data CSV file from OWID.
urlretrieve(owid_covid_url, './data/owid-covid-data.csv')
