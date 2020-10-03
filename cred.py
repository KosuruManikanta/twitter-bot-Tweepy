import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#replace consumer_key,consumer_secret,access_token,access_token_secret 
# with your keys you can get them from your twitter developer account

#follow me on instagaram to get your doubts cleared 
#instagram:- lzy_geek