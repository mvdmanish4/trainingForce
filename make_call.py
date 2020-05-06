import plivo
import json
from rev_ai import apiclient as api

def getConfigFileContent():
	configFile = open("config.json", "r")
	configFileContents = configFile.read()
	configFile.close()

	return json.loads(configFileContents)

def conferenceCall(phoneNumber1, phoneNumber2):
	configFileContents = getConfigFileContent()

	PLIVO_AUTH_ID = configFileContents["plivo-auth-id"]
	PLIVO_AUTH_TOKEN = configFileContents["plivo-auth-token"]
	plivo_number = configFileContents["plivo-phone-number"]

	# Enter the URL of where your conferenceXML.py file is
	answer_url_conference = "https://gentle-garden-81837.herokuapp.com/response/conference"
	answer_url_moderated = "https://gentle-garden-81837.herokuapp.com/response/moderated"
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

def getRevAiAPIClient():
	configFileContents = getConfigFileContent()
	ACCESS_TOKEN = configFileContents["rev-ai-access-token"]
	return api.RevAiAPIClient(ACCESS_TOKEN)

def createTranscriptionLastCall():
	configFileContents = getConfigFileContent()

	PLIVO_AUTH_ID = configFileContents["plivo-auth-id"]
	PLIVO_AUTH_TOKEN = configFileContents["plivo-auth-token"]
	client = plivo.RestClient(PLIVO_AUTH_ID, PLIVO_AUTH_TOKEN)

	response = client.recordings.list(offset=0,limit=1, )
	mp3File = response[0]["recording_url"]

	revAIClient = getRevAiAPIClient()
	job = revAIClient.submit_job_url(media_url=mp3File, skip_diarization=False, skip_punctuation=False)
	job_id = job.id
	return "Job has been created. Job id: " + job_id

def getTranscriptionOfJobId(jobId):
	revAIClient = getRevAiAPIClient()
	job_details = revAIClient.get_job_details(jobId)
	if str(job_details.status) != "JobStatus.TRANSCRIBED":
		return "Still waiting on the job to finish"
	
	# Get transcript as text
	transcript_text = revAIClient.get_transcript_text(jobId)
	return transcript_text
