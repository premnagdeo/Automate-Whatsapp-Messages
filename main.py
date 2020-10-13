from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER, DESTINATION_NUMBER
from twilio.rest import Client
import random
import schedule
import time

texts = [
    "Hi", "Hey", "Hello", "What's up?", "Yo", "Howdy, partner!", "Ahoy, matey!", "How you doin'?",
    "Aloha", "Hola", "You + Me = Coffee shop in 15 minutes?",
]

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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=my_number,
        body=text,
        to=destination_number
    )

    print(message.sid)


# Schedule to send message at noon everyday
schedule.every().day.at("12:00").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
