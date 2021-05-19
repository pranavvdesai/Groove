import tweepy
def twitter_api(twitter_id):
    consumer_key = "kqEFG714jYkuDqGlS3GQyhugY"
    consumer_secret = "jciEcXmxa1fbioXpJWqdbZHauPtqDYhtiVIPDAPKDLX5oQnujn"
    access_token = "1380212929304260608-5X4TT7BunJQ5ggVa39NHTKlKy0z4mW"
    access_token_secret = "gWnRJefFBdBanGzrfG1rryL6xwdQcPo6JTqSeh5zRHIRt"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)

    cursor = tweepy.Cursor(api.user_timeline, id=twitter_id, tweet_mode="extended").items(250)
    tweet_list=""
    for i in cursor:
        tweet_list+=i.full_text
    return tweet_list    

