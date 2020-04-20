from coronavirusData import updateCoronavirusData
from coronavirusTweets import getCoronavirusTweets
import time
import datetime

# List of country codes to run data collection on
countries = ["AU", "CN", "ES", "IT", "US", "VE"]

# infinite loop
while True:
    print("Collecting coronavirus data...")
    # For each country,
    for country_code in countries:
        # Get coronavirus tweets
        getCoronavirusTweets(country_code)

        # Update coronavirus case data csv's
        # updateCoronavirusData(country_code)
    
    # Sleep for 2 hours and then run again
    print("Sleeping for 2 hours at", datetime.datetime.now(), "...")
    time.sleep(7200)
