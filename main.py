""" for Twitter API v2 """

from datetime import datetime
from email import message
from http import client
from pprint import pprint
import tweepy
import keys

client = tweepy.Client(
    consumer_key=keys.API_KEY,
    consumer_secret=keys.API_SECRET,
    access_token=keys.ACCESS_TOKEN,
    access_token_secret=keys.ACCESS_TOKEN_SECRET
)

# message = str(datetime.now())
message = input("tweet: ")
if message == "":
    message = str(datetime.now())


pprint(client.create_tweet(text=message))