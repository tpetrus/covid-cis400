import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

pd.reset_option('display.max_columns')
pd.reset_option('display.max_rows')



deaths_CN = pd.read_csv('C:\School Work\CIS\CIS400\covid-cis400\country_mining\data\CN\CN_coronavirus_data.csv',usecols = [0,1,2,3,4])
deaths_CN
deaths_CN['ID'] = 'CN'
deaths_CN
#No csv data

deaths_ES = pd.read_csv('C:\School Work\CIS\CIS400\covid-cis400\country_mining\data\ES\ES_coronavirus_data.csv')
deaths_ES
deaths_ES['ID'] = 'ES'
deaths_ES

deaths_IT = pd.read_csv('C:\School Work\CIS\CIS400\covid-cis400\country_mining\data\IT\IT_coronavirus_data.csv')
deaths_IT
deaths_IT['ID'] = 'IT'
deaths_IT

deaths_US = pd.read_csv(r'C:\School Work\CIS\CIS400\covid-cis400\country_mining\data\US\US_coronavirus_data.csv')
deaths_US
deaths_US['ID'] = 'US'
deaths_US

deaths_VE = pd.read_csv('C:\School Work\CIS\CIS400\covid-cis400\country_mining\data\VE\VE_coronavirus_data.csv')
deaths_VE
deaths_VE['ID'] = 'VE'
deaths_VE

master_dt = deaths_CN.append(deaths_ES,ignore_index=True).append(deaths_IT,
                            ignore_index=True).append(deaths_US,
                            ignore_index=True).append(deaths_VE,ignore_index=True)
master_dt
master_dt['date'] =pd.to_datetime(master_dt.date)


master_dt.to_csv('master_dt.csv',index=False)

sorted_dt = pd.read_csv('sorted_master.csv')
sorted_dt