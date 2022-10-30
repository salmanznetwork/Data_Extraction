import tweepy
import pandas as pd
import json 
from datetime import datetime
import s3fs 



access_key= "QACxNL5crlQnWaYUzLvHBFStF"
access_secret = "m8UCdEaEl4Nf4Z6hLReRk1JBDeJ6vu3d4b2pRcxeHr2jxEAwN9"
consumer_key = "4832687967-0fEyRmmBHURkbXsSDWZpyJoRwQBIThuyvkmdRru"
consumer_secret = "eD3YmzPlUIkqny6L3CmSIazJvw4caO7eBccR2005vtd3M"


auth= tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)


api= tweepy.API(auth)

tweets = api.user_timeline(screen_name='@elonmusk',
                          count=200,
                          include_rts = False ,
                          tweet_mode = 'extended')

print(tweets)

tweet_list = []
for tweet in tweets:
    text= tweet._json["full_text"]

    refined_tweet={"user": tweet.user.screen_name,
                  'text' : text,
                  'favorite_count' : tweet.favorite_count,
                  'retweet_coutn' : tweet.retweet_count,
                  'created_at ' : tweet.created_at}
    tweet_list.append(refined_tweet)


df = pd.DataFrame(tweet_list)
df.to_csv("ElonMusk_twitter_data.csv") 
