import re
''' regexp module'''

import tweepy 
'''Tweepy module enables Python to communicate with Twitter platform and use its API'''

from tweepy import OAuthHandler
''' To authenticate twitter and get access to tweets posted'''

from textblob import TextBlob
'''It is natural language processing toolkit/module'''

# + 12-NOV-2017 - Swati - added code for authentication on twitter
def init(self):
    ''' keys and tokens from the Twitter Developer Console'''
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    # attempting authentication using twitter API
    try:
        # create OAuthHandler object
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        # set access token and secret
        self.auth.set_access_token(access_token, access_token_secret)
        # create tweepy API object to fetch tweets
        self.api = tweepy.API(self.auth)
    except:
        print("Error: Authentication Failed") #Error occured
# - 12-NOV-2017 - Swati - added code for authentication on twitter

# + 12-NOV-2017 - Swati - Removing spaces special char symbols using python re module
def clean_tweet(self, tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])
                                |(\w+:\/\/\S+)", " ", tweet).split())
# - 12-NOV-2017 - Swati - Removing spaces special char symbols using python re module
