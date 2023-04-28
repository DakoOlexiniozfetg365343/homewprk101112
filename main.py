
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests
from datetime import datetime


uri = "mongodb+srv://lenovodako1980:11082007@cluster0.olvyitf.mongodb.net/?retryWrites=true&w=majority"


client = MongoClient(uri, server_api=ServerApi('1'))


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['temperature_db']
collection = db['temperature_collection']


city = "Kyiv"
api_key = "977d84e0a775c3c9ae5171a8984bef6d"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)


data = response.json()
temp = data['main']['temp']


now = datetime.now()
time_str = now.strftime("%Y-%m-%d %H:%M:%S")


collection.insert_one({"temp": temp, "time": time_str})
print(f"Temperature ({temp} C) inserted into the database at {time_str}")




