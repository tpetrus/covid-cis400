import twitter
from operator import itemgetter

#%%%%%%%%%%%%%%%%%%%%% MINING THE SOCIAL WEB FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%

# ACCESSING TWITTER API
def oauth_login():

    CONSUMER_KEY = 'xsDU3q1jkdAVUVsXcOAzxv7Yl'
    CONSUMER_SECRET = '4jRtiU3LPE1dqHS9wtA2t3VfJ5vK4qF5Yq3KXVs2I9NcYbVDX8'
    OAUTH_TOKEN = '1221184763924484097-Nv92E2q5AltAo1bJ2YHwcmah3D4PHS'
    OAUTH_TOKEN_SECRET = 'fPxEEXgulZZ18Mi9xBQI4ncchIlnD4JbWnGhfhftMtsEX'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

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



