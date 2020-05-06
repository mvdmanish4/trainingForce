import plivo
import json

configFile = open("config.json", "r")
configFileContents = configFile.read()
configFile.close()

configFileContents = json.loads(configFileContents)

PLIVO_AUTH_ID = configFileContents["plivo-auth-id"]
PLIVO_AUTH_TOKEN = configFileContents["plivo-auth-token"]
plivo_number = configFileContents["plivo-phone-number"]

# Enter the URL of where your conferenceXML.py file is
answer_url = "http://127.0.0.1:5000/response/conference"

# Enter the 3 phone numbers you want to join in on the conference call
client = plivo.RestClient(PLIVO_AUTH_ID, PLIVO_AUTH_TOKEN)
conference_numbers = ["14406451698", "14253301518"]
# conference_numbers = ["14253301518"]

for number in conference_numbers:
	response = client.calls.create(from_=plivo_number,to_=number,answer_url=answer_url,answer_method='GET', )
	print(response)