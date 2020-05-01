#Imports
import os
import glob
import pandas as pd

#Set directory
os.chdir(f"/Users/Ryley/Documents/uni/spring20/cis400/project/covid-cis400/country_mining/data/VE/tweet_data/")

#Filename matching
extension = 'csv'
all_filenames = [i for i in glob.glob('VE_04-30-2020_*'.format(extension))]

#Combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#Export to csv
os.chdir(f"/Users/Ryley/Documents/uni/spring20/cis400/project/covid-cis400/country_mining/data/VE/sentiment_data/")
combined_csv.to_csv( "VE_4-30-2020.csv", index=False, encoding='utf-8-sig')

print("CSV created.")