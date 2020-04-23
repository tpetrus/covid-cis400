import pandas as pd
import csv
from matplotlib import pyplot as plt

# List of country codes to run data collection on
countries = ["AU", "CN", "ES", "IT", "US", "VE"]

# List of dates data was collected
dates = ["04-13", "04-14","04-15", "04-16", "04-17", "04-18", "04-19", "04-20"]


#def mergeDayData(country_code, date):
#    tweet_data = pd.read_csv(f"data/{country_code}/sentiment_data/{country_code}_{date}-2020.csv")
#    sentiment_data = pd.read_csv(f"data/{country_code}/sentiment_data/{country_code}_{date}-2020_sentiments.csv")
#    coronavirus_data = pd.read_csv(f"data/{country_code}/{country_code}_coronavirus_data.csv")
#    combined_data = pd.concat([tweet_data, sentiment_data, coronavirus_data], axis=1)
#    print(tweet_data["tweet"])

# Returns the average sentiment value for a given country on a given day
def getAverageSentiment(country_code, date):
    # read sentiment into dataframe
    sentiment_data = pd.read_csv(f"data/{country_code}/sentiment_data/{country_code}_{date}-2020_sentiments.csv")

    # get sum of sentiment values
    sentiment_sum = sentiment_data["sentiment_value"].sum()
    
    # get total number of sentiment values
    sentiment_total = len(sentiment_data.index)
    
    # calculate average sentiment value
    average_sentiment = sentiment_sum/sentiment_total

    return average_sentiment

# Returns the increase in cases between a selected day and the day before
def getIncreaseInCases(country_code, date):
    # read coronavirus data into dataframe
    coronavirus_data = pd.read_csv(f"data/{country_code}/{country_code}_coronavirus_data.csv")

    # convert date to proper format for data
    converted_date = date.replace("-", "/")[1:] + "/20"

    # Get new daily cases for day
    day_data = coronavirus_data.loc[coronavirus_data['date'] == converted_date]
    new_daily_cases = day_data["new_daily_cases"].item()

    # Get new daily cases for day before
    day_index = day_data.index.values.astype(int)[0]
    past_new_daily_cases = coronavirus_data.iloc[ day_index - 1 , 1 ]

    # calculate increase in new daily cases
    increase_in_new_daily_cases = new_daily_cases - past_new_daily_cases

    return float(increase_in_new_daily_cases)

# Prints correlations for given country ****** TODO: Add matplotlib charts ******
def createCorrelationChart(country_code, dates):
    # Create empty dataframe with column names
    country_data = pd.DataFrame(columns = ["date", "average sentiment", "increase in cases from past day"])

    # For each date, add proper data calculations to dataframe
    for date in dates:

        # Get column values
        average_sentiment = getAverageSentiment(country_code, date)
        increase_in_cases = getIncreaseInCases(country_code, date)

        # Create row
        row_df = pd.DataFrame([[date, average_sentiment, increase_in_cases]], columns = ["date", "average sentiment", "increase in cases from past day"])

        # Add row to dataframe
        country_data = country_data.append(row_df, ignore_index=True)

    # Print country's correlation (between -1 and 1)
    print(country_code + ": ", country_data["average sentiment"].corr(country_data["increase in cases from past day"]))



if __name__ == "__main__":
    # get correlation data for each country
    for country in countries:
        createCorrelationChart(country, dates)