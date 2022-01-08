from twilio.rest import Client

TWILIO_SID = "ACe966a446589694915af53f604a835fab"
TWILIO_AUTH_TOKEN = "e7c7c342fec6a85be955b5694fb80884"
TWILIO_VIRTUAL_NUMBER = "+12672147361"
TWILIO_VERIFIED_NUMBER = "+818046419568"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
