#Import the necessary methods from tweepy library
from __builtin__ import file
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
# import json
# import pandas as pd
# import matplotlib.pyplot as plt
# import re

#Variables that contains the user credentials to access Twitter API
access_token = "1389660961-3gJYku0iFwSQeFyZtUYvSitbdXIx3Q4nTeVBApF"
access_token_secret = "sTLZU1GYPZC6A7ZsPZDYWgP3VHABC8XV6I982ZL5sVHTA"
consumer_key = "aYuaVIFsvwO9x4Lb5fPje8wy9"
consumer_secret = "blZjglSqJALWgrqNUhPEyJ8DirDNCYBzPkA0Q5jsO9dtUVP4TF"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    # file = open('datafile.txt', 'w')
    def on_data(self, data):

        # file = open("datafile.txt", "w")
        # file.write(data)


        f = open('datafile.txt', 'w')
        if f is not None:
            with open('datafile.txt','w') as f:
                f.write(data)
        else:
            f.close()

        print data



        #read the data in into an array
        #tweets_data_path = 'datafile.txt'
        # tweets_data = []
        # tweets_file = open("datafile.txt", "r")
        # for line in tweets_file:
        #     try:
        #         tweet = json.loads(line)
        #         tweets_data.append(tweet)
        #     except:
        #         continue
        # print len(tweets_data)
        # tweets = pd.DataFrame()
        # tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
        # print tweets['text']
        return True

    def on_error(self, status):
        print status




if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords:
    #stream.filter(track=['java', 'javascript', 'python'])

    stream.filter(track=['java', 'javascript', 'python'])

