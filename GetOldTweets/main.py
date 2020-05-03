import GetOldTweets3 as got
import timeit
import time
import csv

countries = ['Australia', 'China', 'Spain', 'Italy', 'United States', 'Venezuela']
#The approx mileage for each country radius to collect tweets from
country_radius = ["2500mi", "3250mi", "675mi", "250mi", "2500mi", "500mi"]
country_code = ['AU', 'CN', 'ES', 'IT', 'US', 'VE']

month = 4
date = 1
within = 0
code = 0

for country in countries:
        print(country)

        while date <= 12:

                print('2020-'+ str(month) + '-' + str(date))

                #GetOldTweets setup
                tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Coronavirus')\
                                                                                   .setLang('en')\
                                                                                   .setNear(country)\
                                                                                   .setSince("2020-"+ str(month) + "-" + str(date))\
                                                                                   .setUntil("2020-"+ str(month) + "-" + str(date+1))\
                                                                                   .setMaxTweets(10000)\
                                                                                   .setWithin(country_radius[within])
        
                tweet = got.manager.TweetManager.getTweets(tweetCriteria, bufferLength = 10000)
                print("Collecting Tweets:", len(tweet))

                date2 = "04-0" + str(date) + "-2020"

                date += 1

                #Places the tweets into a csv file for sentiment analysis
                if len(tweet) != 0:
                        with open(f"{country}/{country_code[code]}_{date2}.csv", 'w',  encoding='utf-8') as fd:
                                writer = csv.writer(fd)
                                writer.writerow(["tweet"])
                                for tweets in tweet:
                                        text = tweets.text.replace('\n', ' ').replace('\r', '')
                                        writer.writerow([text])
                                        
                print("Sleeping")
                time.sleep(600)

        date = 1
        within += 1
        code += 1
