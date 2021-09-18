import tweepy
from dotenv import load_dotenv
import os
load_dotenv()


def twitter_api(twitter_id):
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    cursor = tweepy.Cursor(api.user_timeline, id=twitter_id,
                           tweet_mode="extended").items(250)
    tweet_list = ""
    for i in cursor:
        tweet_list += i.full_text
    return tweet_list
