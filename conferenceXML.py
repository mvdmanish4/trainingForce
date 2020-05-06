from flask import Flask, Response, request, url_for 
from plivo import plivoxml
from bs4 import BeautifulSoup
app=Flask(__name__) 

@app.route('/response/conference/', methods=['GET']) 
def conference():
	response = plivoxml.ResponseElement()
	response.add(plivoxml.ConferenceElement('My Room', end_conference_on_exit=True))
	soup = BeautifulSoup(response.to_string(), "xml")
	return Response(str(soup.prettify()), mimetype='text/xml')

if __name__ == "__main__":
	app.debug = True
	app.run()