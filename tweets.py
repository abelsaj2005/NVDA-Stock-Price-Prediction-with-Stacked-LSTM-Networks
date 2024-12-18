from twikit import Client, TooManyRequests
import time
from datetime import datetime
import csv
from configparser import ConfigParser
from random import randint
import asyncio

MINIMUM_TWEETS = 10

QUERY = 'AAPL'

config = ConfigParser()
config.read('config.ini')
username = config['X']['username']
email = config['X']['email']
password = config['X']['password']

client = Client(language='en-US')

client.login(auth_info_1=username, auth_info_2=email, password=password)
client.save_cookies('cookies.json')

client.load_cookies('cookies.json')

tweets = client.search_tweet(QUERY, product='Top')

for tweet in tweets:
    print(vars(tweet))
    break

