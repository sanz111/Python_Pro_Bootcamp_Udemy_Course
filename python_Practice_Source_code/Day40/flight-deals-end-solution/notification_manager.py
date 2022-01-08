import smtplib
from twilio.rest import Client

TWILIO_SID = "ACe966a446589694915af53f604a835fab"
TWILIO_AUTH_TOKEN = "e7c7c342fec6a85be955b5694fb80884"
TWILIO_VIRTUAL_NUMBER = "+12672147361"
TWILIO_VERIFIED_NUMBER = "+818046419568"

MAIL_PROVIDER_SMTP_ADDRESS ="smtp.gmail.com"
MY_EMAIL = "jackma22336677@gmail.com"
MY_PASSWORD = "4$dbxxr#i!HtN3G9"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )