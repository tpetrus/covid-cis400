from cookbook import oauth_login, twitter_search
from coronavirusData import updateCoronavirusData
import xlsxwriter


# Fetches 1100 most recent coronavirus tweets from US, CN, and ES
def getCoronavirusTweets():
	twitter_api = oauth_login()

	q = "Coronavirus"

	workbook = xlsxwriter.Workbook('term_project.xlsx')
	worksheet = workbook.add_worksheet()

	# United States (US)
	# China (CN)
	# Spain (ES)

	countries = [(0, "US"), (1, "CN"), (2, "ES")]

	for country in countries:
		results = twitter_search(twitter_api, q, max_results=1000, lang="en", place_country=country[1])
		status_texts = [status["text"] for status in results]

		row = 0
		for text in status_texts:
			worksheet.write(row, country[0], text)
			row +=1
		
	workbook.close()

# Get coronavirus tweets
getCoronavirusTweets()

# Update coronavirus csv's
updateCoronavirusData()
