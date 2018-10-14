#!/usr/bin/python
from twython import Twython, TwythonError 
from time import sleep
from credentials import *

twitter = Twython(app_key, app_secret, access_token, access_token_secret)

"""
for follower in tweepy.Cursor(api.followers).items():
    if not follower.following:
        follower.follow()
        print ("Followed everyone that is following @" + user.name)
        sleep(1800)
"""

def retweet_fav(query):
    print("Retweeting and Favoriting: " + query)
    result = twitter.search(q=query, count=50, since="2018-10-07")
    for tweet in result["statuses"]:
        try:
            twitter.create_favorite(id = tweet["id_str"])
            print('Favorited')
            #print('Favorited the tweet by @' + tweet.user.screen_name)
            twitter.retweet(id = tweet["id_str"])
            #print('Retweeted the tweet by @' + tweet.user.screen_name)
            print('Retweeted')
            sleep(60)

        except TwythonError as e:
            print(e)

        except StopIteration:
            break

retweet_fav(query="#FateCore")
retweet_fav("#FateAccelerated")
retweet_fav("#FateRPG")
