# Download the helper library from https://www.twilio.com/docs/python/install
import twilio
import twilio.rest
from twilio.rest import Client
import json

configFile = open("config.json", "r")
configFileContents = configFile.read()
configFile.close()

configFileContents = json.loads(configFileContents)
account_sid = configFileContents["twilio-account-sid"]
auth_token = configFileContents["twilio-auth-token"]
client = Client(account_sid, auth_token)

dialogflowPhoneNumber = configFileContents["dialogflow-phone-number"]

call = client.calls.create(url='http://demo.twilio.com/docs/classic.mp3',to=dialogflowPhoneNumber, from_='+14406451698')

print(call.sid)