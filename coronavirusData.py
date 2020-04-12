import http.client
import mimetypes
import json
import csv


# list of countries to fetch data for
countries = ["US", "CN", "ES"]

# Fetch country data as JSON object for specified country
def getCountryData(country_code):
    conn = http.client.HTTPSConnection("api.thevirustracker.com")
    conn.request("GET", f"/free-api?countryTimeline={country_code}", '', {})
    res = conn.getresponse()
    data = res.read()
    data_object = json.loads(data)
    return data_object


# save data for each country to CSV
def updateCoronavirusData():
    for country in countries:
        with open(f"data/{country}_coronavirus_data.csv", 'w') as fd:
            writer = csv.writer(fd)

            # Write header row
            writer.writerow(["date", "new_daily_cases", "new_daily_deaths", "total_cases", "total_recoveries", "total_deaths"])

            # fetch data
            data = getCountryData(country)

            # trim data
            trimmed_data = data["timelineitems"][0]
            del trimmed_data["stat"]

            # iterate through data and save to csv
            for date, data in trimmed_data.items():
                values = [val for val in data.values()]
                newRow = [date] + values
                writer.writerow(newRow)

            print(f"saved {country} data to csv.")