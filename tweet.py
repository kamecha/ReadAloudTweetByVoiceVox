import tweepy
import os

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
USER_ID = os.getenv('USER_ID')

# 認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# api取得
api = tweepy.API(auth, wait_on_rate_limit=True)
api.verify_credentials()

latestId = api.home_timeline(count=1)[0].id
while True:
    home = api.home_timeline(
        since_id=latestId, include_entities=False, exclude_replies=True)
    for tweet in home:
        latestId = tweet.id
        print(tweet.id)
        print(tweet.created_at)
        print(tweet.text)
        print('\n')
