import csv
import tweepy
from cred import *

woeid = 2295414

trends = api.trends_place(id=woeid)

print("The top trends for the location are :")

for value in trends:
    for trend in value['trends']:
        print(trend['name'])


#woeid woeid is a unique code set for locations search for woeid code of the location you want in google
#here woeid code 2295414 belongs to hyderabad India