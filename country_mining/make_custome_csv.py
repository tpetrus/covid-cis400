import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

pd.reset_option('display.max_columns')
pd.reset_option('display.max_rows')

deaths_CN = pd.read_csv('C:\School Work\CIS\CIS400\covid-cis400\country_mining\data\CN\CN_coronavirus_data.csv')
#No csv data

deaths_ES = pd.read_csv('C:\School Work\CIS\CIS400\covid-cis400\country_mining\data\ES\ES_coronavirus_data.csv')
deaths_ES


deaths_IT = pd.read_csv('C:\School Work\CIS\CIS400\covid-cis400\country_mining\data\IT\IT_coronavirus_data.csv')
deaths_IT

deaths_US = pd.read_csv('C:\School Work\CIS\CIS400\covid-cis400\country_mining\data\US\US_coronavirus_data.csv')
deaths_US #Problem here reading csv

deaths_VE = pd.read_csv('C:\School Work\CIS\CIS400\covid-cis400\country_mining\data\VE\VE_coronavirus_data.csv')
deaths_VE

def fill_rows(dataframe,country_name):
        dataframe[:,-1] = country_name
        dasdsadsad