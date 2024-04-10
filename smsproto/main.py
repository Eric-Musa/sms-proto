
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


# Download the helper library from https://www.twilio.com/docs/python/install

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

twilio_number = os.environ['TWILIO_NUMBER']
personal_number = os.environ['PERSONAL_NUMBER']

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=twilio_number,
                     to=personal_number
                 )

print(message.sid)

client.messages.get