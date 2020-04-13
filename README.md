# covid-cis400

## **Setup:**

### How To Create Twitter API Config File:

- Go to country_mining dir: `cd country_mining`
- Create file: `touch api_config.py`
- Paste below skeleton code into api_config.py
- Input all values for your twitter developer account in api_config object. These can be found under "Keys and tokens" in your twitter developer app
- Save, then run the file `python api_config.py`

**IMPORTANT:** Do not move this file or the resulting api_config.pkl or your API keys will show up on our public GitHub
**IMPORTANT 2:** This file only needs to be run once unless your api config values change.

**api_config.py:**

```
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
```

## **To Collect Data:**

- Go to ./country_mining
- Run `python main.py`\*

  \* New tweets will automatically be fetched every 2 hours for every country while program is running
