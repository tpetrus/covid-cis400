#Imports
import pandas as pd
import numpy as np
import csv
import re
from textblob import TextBlob

#Set country code dates
country_date1 = "4-21-2020"
country_date2 = "4-22-2020"
country_date3 = "4-23-2020"
country_date4 = "4-24-2020"
country_date5 = "4-25-2020"
country_date6 = "4-26-2020"
country_date7 = "4-27-2020"
country_date8 = "4-28-2020"
country_date9 = "4-29-2020"
country_date10 = "4-30-2020"
country_date11 = "05-01-2020"

#List of country codes
country_code = [country_date1, country_date2, country_date3, country_date4, country_date5, country_date6, country_date7, country_date8, country_date9, country_date10, country_date11]

#Clean the tweet
def clean_tweet(tweet):
       return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


#Analyze the tweet
def analyze_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1
    
#Iterate through tweets
for date in country_code:
    with open(f"/Users/Ryley/Documents/uni/spring20/cis400/project/covid-cis400/country_mining/data/VE/sentiment_data/VE_{date}.csv", 'r') as _filehandler:
        csv_file_reader = csv.DictReader(_filehandler) #read CSV file tweets
        i = next(csv_file_reader)
        print(i)
        with open(f"/Users/Ryley/Documents/uni/spring20/cis400/project/covid-cis400/country_mining/data/VE/sentiment_data/VE_{date}_sentiments.csv", 'w',  encoding='utf-8') as fd:
            writer = csv.writer(fd)
            writer.writerow(['sentiment_value']) #write value of sentiment header
            for row in csv_file_reader: #clean and analyze each tweet
                #i = next(csv_file_reader)
                #print(i)
                tweet = row["\ufefftweet"]
                clean_tweet(tweet)
                text = analyze_sentiment(tweet) #set text to tweet sentiment
                writer.writerow([text])
    print("File created.")

