from os import environ
from flask import Flask
import bot

app = Flask(__name__)

@app.route("/")
def home():
    bot.tweet_quote()
    return "Tweeting a GOT Quote..."

app.run(host= '0.0.0.0', port=environ.get('PORT'))