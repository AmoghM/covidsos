import os
import tweepy as tw
import pandas as pd
import yaml

with open("../configs/keys.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

key = cfg['twitter']

consumer_key = key['consumer_key']
consumer_secret = key['consumer_secret']
access_token = key['access_token']
access_token_secret = key['access_token_secret']

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

def get_tweets(search_words, date_since, size = 5):
    # Define the search term and the date_since date as variables
    
    new_search = search_words + " -filter:retweets"

    tweets = tw.Cursor(api.search,
                q=new_search,
                lang="en",
                since=date_since).items(size)

    # Iterate and print tweets
    res = []
    for tweet in tweets:
        res.append(tweet.text)
    
    return res