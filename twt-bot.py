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
    duplicates = 0
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
            if "403 (Forbidden)" in str(e):
                duplicates += 1
            else:
                print("  " + str(e))

        except StopIteration:
            break
    print("  " + str(duplicates) + " duplicate(s) found")

# Keep the program running
while 1:
    retweet_fav(query="#FateCore")
    retweet_fav("#FateAccelerated")
    retweet_fav("#FateRPG")
    counter = 30
    while counter > 0:
        print(str(counter) + " minutes until next scan")
        counter -= 5
        sleep(300)

