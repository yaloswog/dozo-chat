# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACce5ef378df1d9e2f92cb75627d2a4ea9']
auth_token = os.environ['548550a1d64db785b289cf0713db86d2']
client = Client(account_sid, auth_token)

conversation = client.conversations \
                     .v1 \
                     .conversations \
                     .create(friendly_name='My First Conversation')

print(conversation.sid)