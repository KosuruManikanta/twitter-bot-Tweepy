import tweepy
import simplejson as json
from cred import *

# ID of the recipient
recipient_id ="1311264755177279493"

# text to be sent
text = "This is a Direct Message."


# sending the direct message
direct_messages = api.send_direct_message(recipient_id, text)
print(direct_messages)

#follow me on instagaram to get your doubts cleared 
#instagram:- lzy_geek

