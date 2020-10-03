import tweepy
import simplejson as json
from cred import *

last_dms = api.list_direct_messages(2) #number specifies number of messages you want to fetch
for messages in last_dms:
    u = api.get_user(messages.message_create['sender_id'])
    print(u.name +":" +messages.message_create['message_data']['text'])
    #print(messages)

#replace 2 in line 5 with what so ever number you like which is > 0 depends upon how many messages you want to read.

#follow me on instagaram to get your doubts cleared 
#instagram:- lzy_geek