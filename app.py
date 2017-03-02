import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question
import os
import requests

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def new_session():
    welcome_msg = "hello"
    return statement(welcome_msg)

@ask.intent("AllIntent", convert={'All': str})
def next_round(All):
    try:
        response = requests.post(os.environ['DISCRIMINATOR_URI'], data={'text': All})
        return question(response.text)
    except KeyError, requests.exceptions.RequestException:
        return statement("I'm sorry. My servers aren't available at this
                         time.")
@ask.intent("AMAZON.StopIntent")
def stop():
    return statement("goodbye")

@ask.intent("AMAZON.HelpIntent")
def help():
	return question("I'm Eigen, ask me anything.")

@ask.session_ended
def session_ended():
    return statement("goodbye")

if __name__ == '__main__':
    app.run(debug=True)
