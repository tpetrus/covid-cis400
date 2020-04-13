import twitter
from operator import itemgetter
import pickle
import sys

#%%%%%%%%%%%%%%%%%%%%% MINING THE SOCIAL WEB FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%

# ACCESSING TWITTER API
def oauth_login():

    try:
        # Fetch API config object from pickle
        with open('api_config.pkl', 'rb') as api_config_pkl:
            api_config = pickle.load(api_config_pkl)
    
    # Make sure api config file is set up
    except FileNotFoundError: 
        print("Error: twitter api config file not set up properly. View project README or ./country_mining/api_config.py for setup instructions")
        sys.exit()
        
    auth = twitter.oauth.OAuth(api_config["OAUTH_TOKEN"], api_config["OAUTH_TOKEN_SECRET"],
                               api_config["CONSUMER_KEY"], api_config["CONSUMER_SECRET"])

    twitter_api = twitter.Twitter(auth=auth)

    return twitter_api

# SEARCHING FOR TWEETS
def twitter_search(twitter_api, q, max_results=200, **kw):

    # See https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
    # and https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators
    # for details on advanced search criteria that may be useful for 
    # keyword arguments
    
    # See https://dev.twitter.com/docs/api/1.1/get/search/tweets    
    search_results = twitter_api.search.tweets(q=q, count=100, **kw)
    
    statuses = search_results['statuses']
    
    # Iterate through batches of results by following the cursor until we
    # reach the desired number of results, keeping in mind that OAuth users
    # can "only" make 180 search queries per 15-minute interval. See
    # https://developer.twitter.com/en/docs/basics/rate-limits
    # for details. A reasonable number of results is ~1000, although
    # that number of results may not exist for all queries.
    
    # Enforce a reasonable limit
    max_results = min(1000, max_results)
    
    for _ in range(10): # 10*100 = 1000
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError as e: # No more results when next_results doesn't exist
            break
            
        # Create a dictionary from next_results, which has the following form:
        # ?max_id=313519052523986943&q=NCAA&include_entities=1
        kwargs = dict([ kv.split('=') 
                        for kv in next_results[1:].split("&") ])
        
        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']
        
        if len(statuses) > max_results:
            print("Number of Tweets: ",len(statuses)) 
            break
            
    return statuses



