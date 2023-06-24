from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

# Twilio account credentials
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    # Get the phone number from the request
    phone_number = request.form.get('phone_number')

    try:
        # Send the SMS using Twilio
        message = client.messages.create(
            body='Hello',
            from_=twilio_phone_number,
            to=phone_number
        )
        return 'SMS sent successfully.'
    except Exception as e:
        return 'Failed to send SMS. Error: {}'.format(str(e))

if __name__ == '__main__':
    app.run(debug=True)
