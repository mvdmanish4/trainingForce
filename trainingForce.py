# -*- coding: utf-8 -*-
from flask import Flask, Response, request, url_for
import wikipedia
from flask import send_file
import numpy as np
import matplotlib.pyplot as plt
import json, requests
from random import randint
from flask import jsonify
import smtplib
from smtplib import SMTPException
from plivo import plivoxml
from bs4 import BeautifulSoup
import make_call

app = Flask(__name__)

@app.route("/")
def hello():
	return "Home"

@app.route("/sentScore")
def sentimentScore():
	return "Return Sentiment Score"

#http://127.0.0.1:5000/data?user=some-value
@app.route('/data')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.get('user')
    return user

@app.route("/Data")
def geData():
	url = 'https://www.quandl.com/api/v3/datatables/SHARADAR/SF1.json?ticker=AAPL&calendardate=2015-12-31&dimension=MRY&api_key=WyHRuMayFcNMsuCyMYSz'
	resp = requests.get(url=url)
	return resp.content

def responseToXML(response):
	xml = BeautifulSoup(response.to_string(), "xml")
	return Response(str(xml.prettify()), mimetype='text/xml')

@app.route('/response/conference/', methods=['GET']) 
def conference():
	response = plivoxml.ResponseElement()
	response.add(plivoxml.ConferenceElement('My Room',start_conference_on_enter=False,wait_sound='https://youtu.be/fu8Zrf9bS38'))
	return responseToXML(response)

@app.route('/response/moderated/', methods=['GET'])
def moderated():
	response = plivoxml.ResponseElement()
	response.add(plivoxml.ConferenceElement('My Room',start_conference_on_enter=True,end_conference_on_exit=True))
	return responseToXML(response)

@app.route('/makeCall')
def makeCall():
	phoneNumber1 = request.args.get('phoneNumber1')
	if not request.args.get('phoneNumber2'):
		phoneNumber2 = ""
	else:
		phoneNumber2 = request.args.get('phoneNumber2')

	make_call.conferenceCall(phoneNumber1, phoneNumber2)
	return "Success"

if __name__ == "__main__":
	app.debug = True
	app.run()