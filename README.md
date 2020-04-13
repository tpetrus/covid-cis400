# covid-cis400

## **Setup:**

### How To Create Twitter API Config File:

- `cd country_mining`
- Open `api_config.py`
- Input all values for your twitter developer account in api_config object. These can be found under "Keys and tokens" in your twitter developer app
- Save, then run the file `python api_config.py`

**IMPORTANT:** Do not move this file or the resulting api_config.pkl or your API keys will show up on our public GitHub
**IMPORTANT 2:** This file only needs to be run once unless your api config values change.

## **To Collect Data:**

- Go to ./country_mining
- Run `python main.py`\*

  \* New tweets will automatically be fetched every 2 hours for every country while program is running
