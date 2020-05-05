# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_mysqldb import MySQL
import wikipedia
from flask import send_file
import numpy as np
import matplotlib.pyplot as plt
import urllib2
import json, requests
from random import randint
from flask import jsonify
import smtplib
from smtplib import SMTPException

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

if __name__ == "__main__":
	app.debug = True
	app.run()