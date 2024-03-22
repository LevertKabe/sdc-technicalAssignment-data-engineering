import requests
import os
import pandas as pd
import json
from dotenv import load_dotenv
from datetime import date, datetime, timedelta

load_dotenv('/Users/levert/Code/Data Projects/ringier/sdc-technicalAssignment-data-engineering/secrets-file/.env')

NEWS_API_KEY= os.getenv('NEWS_API_KEY')

last_week = datetime.now() - timedelta(days=7)

start = last_week - timedelta(days=last_week.weekday())
end = start + timedelta(days=6)
from_date = start.strftime('%Y-%m-%d')

to_date = end.strftime('%Y-%m-%d')
print(start.strftime('%Y-%m-%d'))
print(end.strftime('%Y-%m-%d'))

print(NEWS_API_KEY)
url_string = 'https://newsapi.org/v2/everything?q=apple&from=' + from_date + '&to=' + to_date + '&sortBy=popularity&apiKey=' + NEWS_API_KEY
url = (url_string)
response = requests.get(url)
#print(response.json())

elevations = response.json()

data = json.dumps(elevations['articles'])

df = pd.json_normalize(elevations['articles'], errors='ignore')

print(df)

