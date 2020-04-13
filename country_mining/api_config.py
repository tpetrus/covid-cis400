import pickle

# How To Create Config File:
#  - Input all values for your twitter developer account below. These can
#    be found under "Keys and tokens" in your twitter developer app
#  - Run this file (`python api_config.py`)
# IMPORTANT: Do not move this file or the resulting api_config.pkl or your
# API keys will show up on our public GitHub
# IMPORTANT 2: This file only needs to be run once unless your api config values change.


# input API details for your Twitter Developer account
api_config = {
    'CONSUMER_KEY': '',
    'CONSUMER_SECRET': '',
    'OAUTH_TOKEN': '',
    'OAUTH_TOKEN_SECRET': ''
}

# Dump api_config object to pickle file
with open('api_config.pkl', 'wb') as pkl:
    pickle.dump(api_config, pkl)