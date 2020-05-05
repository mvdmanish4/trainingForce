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

@app.route("/setInent")
def setIntent():
	return "Return Set Intent"

if __name__ == "__main__":
	app.debug = True
	app.run()