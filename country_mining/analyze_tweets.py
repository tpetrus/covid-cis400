#Imports
import pandas as pd 
import numpy as np
import csv
import re
from textblob import TextBlob

#Set country code dates 
AU_date = "04-12-2020_21-05"
CN_date = "04-12-2020_21-05"
ES_date = "04-12-2020_21-05"
IT_date = "04-12-2020_21-05"
US_date = "04-12-2020_21-06"
VE_date = "04-12-2020_21-06"

#List of country codes
country_code = {"AU": AU_date, "CN": CN_date, "ES": ES_date, "IT": IT_date, "US": US_date, "VE": VE_date}

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
for country, date in country_code.items():
    with open(f"/Users/Ryley/Documents/uni/spring20/cis400/project/covid-cis400/country_mining/data/{country}/tweet_data/{country}_{date}.csv", 'r') as _filehandler: 
        csv_file_reader = csv.DictReader(_filehandler) #read CSV file tweets
        with open(f"/Users/Ryley/Documents/uni/spring20/cis400/project/covid-cis400/country_mining/data/{country}/tweet_data/{country}_sentiments_TEST.csv", 'w',  encoding='utf-8') as fd:
            writer = csv.writer(fd) 
            writer.writerow(['sentiment_value']) #write value of sentiment header 
            for row in csv_file_reader: #clean and analyze each tweet
                tweet = row['tweet']
                clean_tweet(tweet)
                text = analyze_sentiment(tweet) #set text to tweet sentiment
                writer.writerow([text])
    print("File created.")