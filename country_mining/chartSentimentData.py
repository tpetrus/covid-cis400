from matplotlib import pyplot as plt
import pandas as pd
import csv

neutral = 0
positive = 0
negative = 0
newData = []
country = "VE"
dates =["13", "14", "15", "16","17","18","19","20"]

for date in dates:
    with open(f"covid-cis400/country_mining/data/{country}/sentiment_data/{country}_04-{date}-2020_sentiments.csv", newline='') as f:
        reader = csv.reader(f)
        for row in reader: 
            newData.append(row[0])
    

                
for y in newData: 
    if y == '0':
        neutral += 1
    elif y == '-1':
        negative += 1
    elif y == '1':
        positive += 1

print(neutral, negative, positive)

#Plot the 
fig = plt.figure()
#ax = fig.title("AU Neutral, Negative, and Positive Tweets from 4/13/2020 to 4/20/2020")
ax = fig.add_axes([0,0,1,1])
values = ['Neutral', 'Negative', 'Positive']
tweets = [neutral, negative, positive]
ax.bar(values, tweets)
plt.show()
