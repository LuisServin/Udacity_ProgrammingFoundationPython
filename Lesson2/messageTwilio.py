# !usr/bin/env python

# import the twilio library
from twilio.rest import TwilioRestClient

account_ssid = "AC6c1e02aa57256168bc51a07b9cbd41a6"
auth_token = "5ecac3541f89512d0bceec495c95327f"
client = TwilioRestClient(account_ssid,auth_token)

message = client.sms.messages.create(
	body = "Trying twilio!!",
	to = "+5215548218909",
	from_ = "+18036755677")

print message.sid