import tweepy
import csv

from cred import *


class TwitterStreamListener(tweepy.streaming.StreamListener):
    ''' Handles data received from the stream. '''
    def on_status(self, status,count=0):
        with open('twitter.csv', 'a') as csvfile:     #refer note in the down for explanation
            fieldnames = ['id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'id': status.user.id})
        print(status)
       # print(status.user.name+":"+status.text)
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
listener = TwitterStreamListener()
public_tweets = api.home_timeline()
stream = tweepy.streaming.Stream(auth, listener)
stream.filter(track=["#INDvWI"])


#from line 7 to 11 we are opening a csv file and writing ID's of user for future usage
# if required you can use else you can remove those lines that wont effect the output
# but data wont be stored in twitter.csv


#follow me on instagaram to get your doubts cleared 
#instagram:- lzy_geek