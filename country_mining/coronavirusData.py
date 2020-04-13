import http.client
import mimetypes
import json
import csv


# list of countries to fetch data for

# Fetch country data as JSON object for specified country
def getCountryData(country_code):
    conn = http.client.HTTPSConnection("api.thevirustracker.com")
    conn.request("GET", f"/free-api?countryTimeline={country_code}", '', {})
    res = conn.getresponse()
    data = res.read()
    data_object = json.loads(data)
    return data_object


# save data for each country to CSV
def updateCoronavirusData(country_code):
        with open(f"data/{country_code}/{country_code}_coronavirus_data.csv", 'w') as fd:
            writer = csv.writer(fd)

            # Write header row
            writer.writerow(["date", "new_daily_cases", "new_daily_deaths", "total_cases", "total_deaths"])

            # fetch data
            data = getCountryData(country_code)

            # trim data
            trimmed_data = data["timelineitems"][0]
            del trimmed_data["stat"]

            # iterate through data and save to csv
            for date, data in trimmed_data.items():
                del data["total_recoveries"] # total recovery data is currently broken in API
                values = [val for val in data.values()]
                newRow = [date] + values
                writer.writerow(newRow)

            print(f"saved {country_code} data to csv.")