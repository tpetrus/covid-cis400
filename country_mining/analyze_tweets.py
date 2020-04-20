#Imports
import pandas as pd
import numpy as np
import csv
import re
from textblob import TextBlob

#Set country code dates
country_date1 = "04-13-2020"
country_date2 = "04-14-2020"
country_date3 = "04-15-2020"
country_date4 = "04-16-2020"
country_date5 = "04-17-2020"
country_date6 = "04-18-2020"
country_date7 = "04-19-2020"
country_date8 = "04-20-2020"

#List of country codes
country_code = [country_date1, country_date2, country_date3, country_date4, country_date5, country_date6, country_date7, country_date8]

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
        with open(f"/Users/Ryley/Documents/uni/spring20/cis400/project/covid-cis400/country_mining/data/VE/sentiment_data/VE_{date}_sentiments.csv", 'w',  encoding='utf-8') as fd:
            writer = csv.writer(fd)
            writer.writerow(['sentiment_value']) #write value of sentiment header
            for row in csv_file_reader: #clean and analyze each tweet
                tweet = row['tweet']
                clean_tweet(tweet)
                text = analyze_sentiment(tweet) #set text to tweet sentiment
                writer.writerow([text])
    print("File created.")
