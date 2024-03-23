import requests
import os
import pandas as pd
import json
from dotenv import load_dotenv
from datetime import date, datetime, timedelta
import mysql.connector

load_dotenv('/src/secrets-file/.env')

NEWS_API_KEY= os.getenv('NEWS_API_KEY')

db = mysql.connector.connect(host = 'mydb', user = 'root', password = 'root', port = 3306)
print("DB connected")

print("DB connected")
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

df = pd.json_normalize(elevations['articles'], errors='ignore')

print(df)




