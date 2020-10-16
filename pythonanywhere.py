from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER, DESTINATION_NUMBER
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import random
import schedule
import time
import os

# Get the texts from texts.txt
texts = []
with open('texts.txt') as f:
    texts = f.readlines()
texts = [text.strip() for text in texts]


# Proxy configuration for PythonAnywhere. Reference: https://help.pythonanywhere.com/pages/TwilioBehindTheProxy
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

# Configuration variables
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
my_number = TWILIO_NUMBER
destination_number = DESTINATION_NUMBER


# Function to send messages
def send_message():
    # Choose random text from texts
    text = random.choice(texts)

    # Create a connection and send message
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        from_=my_number,
        body=text,
        to=destination_number
    )

    print(message.sid)


# Schedule to send message at noon everyday.
# Docs for schedule: https://schedule.readthedocs.io/
schedule.every().day.at("12:00").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
