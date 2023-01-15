'''
This notebook shows some examples of analyzing tabular data with Pandas.
The source CSV is Our World in Data Covid data. 
'''

from urllib.request import urlretrieve
import os
import pandas as pd

owid_covid_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

# Create the data folder under current directory.
os.makedirs('./data', exist_ok=True)

# Download the covid data CSV file from OWID.
urlretrieve(owid_covid_url, './data/owid-covid-data.csv')

covid_df = pd.read_csv('./data/owid-covid-data.csv')

# Select specific columns from the initial data frame.
covid1_df = covid_df[['date','location','new_cases','new_deaths','icu_patients','new_tests','people_vaccinated','people_fully_vaccinated','new_vaccinations','population']]

# Select rows for specific locations.
canada = covid1_df.location == 'Canada'
romania = covid_df.location == 'Romania'

# Select data for specific locations.
covid_ca = covid1_df[canada]
covid_ro = covid1_df[romania]
