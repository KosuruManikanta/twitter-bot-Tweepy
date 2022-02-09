import csv
import tweepy
from cred import *
with open('twitter.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      u= api.get_user(row['id'])
      print(u.location)

#here i stored ID's of those who are tweeting about the particular hashtag in hashtagstream.py file and using 
# that here if you want to search single user then simply import tweepy and cred and then simply write line 7 and 8.
#in line 7 replace row['id'] with screen name or id.


#follow me on instagaram to get your doubts cleared 
#instagram:- lzy_geek
