#!/usr/bin/python
from twython import Twython, TwythonError 
from time import sleep
from credentials import *

twitter = Twython(app_key, app_secret, access_token, access_token_secret)

def retweet_fav(query):
    print("Retweeting and Favoriting: " + query)
    result = twitter.search(q=query, result_type="latest", count=50, since="2018-10-07")
    duplicates = 0
    for tweet in result["statuses"]:
        try:
            twitter.create_favorite(id = tweet["id_str"])
            twitter.retweet(id = tweet["id_str"])
            print('Favorited & Retweeted')
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
        print("  " + str(counter) + " minutes until next scan")
        counter -= 5
        sleep(300)

