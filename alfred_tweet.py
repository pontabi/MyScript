import os
import tweepy
import sys

query = sys.argv[1]

bearer_token = os.environ["X_BEARER_TOKEN"]
consumer_key = os.environ["X_CONSUMER_KEY"]
consumer_secret = os.environ["X_CONSUMER_SECRET"]
access_token = os.environ["X_ACCESS_TOKEN"]
access_token_secret = os.environ["X_ACCESS_TOKEN_SECRET"]

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

response = client.create_tweet(
    text=query
)
print(f"https://twitter.com/user/status/{response.data['id']}")
