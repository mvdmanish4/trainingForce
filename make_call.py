import plivo
import json

def conferenceCall(phoneNumber1, phoneNumber2):
	configFile = open("config.json", "r")
	configFileContents = configFile.read()
	configFile.close()

	configFileContents = json.loads(configFileContents)

	PLIVO_AUTH_ID = configFileContents["plivo-auth-id"]
	PLIVO_AUTH_TOKEN = configFileContents["plivo-auth-token"]
	plivo_number = configFileContents["plivo-phone-number"]

	# Enter the URL of where your conferenceXML.py file is
	# TODO Fix this URL
	answer_url_conference = "http://127.0.0.1:5000/response/conference"
	answer_url_moderated = "http://127.0.0.1:5000/response/moderated"

	# Enter the 3 phone numbers you want to join in on the conference call
	client = plivo.RestClient(PLIVO_AUTH_ID, PLIVO_AUTH_TOKEN)

	if not phoneNumber2:
		phoneNumber2 = configFileContents["dialogflow-phone-number"]
	conference_numbers = [phoneNumber1, phoneNumber2]

	for number in conference_numbers:
		if number == phoneNumber1:
			response = client.calls.create(from_=plivo_number,to_=number,answer_url=answer_url_moderated,answer_method='GET', )
		else:
			response = client.calls.create(from_=plivo_number,to_=number,answer_url=answer_url_conference,answer_method='GET', )
		print(response)