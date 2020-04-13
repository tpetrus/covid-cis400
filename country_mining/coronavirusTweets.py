import csv
import datetime
from twitter_mining import oauth_login, twitter_search
import sys


# Fetches most recent coronavirus tweets from country
def getCoronavirusTweets(country_code):
	twitter_api = oauth_login()
	q = "Coronavirus"

	# Default if twitter API doesn't fetch any data
	results = [{"text": "Error: no data retreived from twitter"}]

	# Run twitter API function.  If config file isn't set up, show error message
	try:
		results = twitter_search(twitter_api, q, max_results=10000, lang="en", place_country=country_code)
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		print("Error: twitter api config file not set up properly. View project README or ./country_mining/api_config.py for setup instructions")
		sys.exit()

	# Fetch date in format MM-DD-YYYY_HH-MM
	now = datetime.datetime.now()
	date = now.strftime("%m-%d-%Y_%H-%M")

	# Add tweet data to file in format: {country code}_{MM-DD-YYYY_HH-MM}.csv
	with open(f"data/{country_code}/tweet_data/{country_code}_{date}.csv", 'w',  encoding='utf-8') as fd:
		writer = csv.writer(fd)

		# CSV Header
		writer.writerow(["tweet"])

		# Add tweets to CSV
		for tweet in results:
			# Remove unneeded whitespace
			text = tweet["text"].replace('\n', ' ').replace('\r', '')

			writer.writerow([text])
	