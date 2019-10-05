# Tweet Quote Bot
A twitter bot that tweets a game of thrones quote every 24 hours. The quotes are stored in the `data.json` file as a JSON object.

## Local Development Setup
N.B: You will need to have a twitter developers account. So make sure you already have one or go to [Twitter Developers](https://developer.twitter.com/en/apply-for-access.html)
to create a developer account.
After doing that, you can proceed to doing the steps listed below:

1. Clone project repository
2. Navigate into project repository i.e `cd tweet-quote-bot`
3. Set up a virtual environment for the project: `$ python3 -m venv` or `$ py -3 -m venv`
4. Create a `credentials.py` file
5. Add the following information to it:
  ```
  ACCESS_TOKEN=YOUR-ACCESS-TOKEN
  ACCESS_TOKEN_SECRET=YOUR-ACCESS-TOKEN-SECRET
  API_KEY=YOUR-API-KEY
  API_SECRET_KEY=YOUR-API-SECRET-KEY
  ```
  6. Install the requirements: 
    `$ pip install -r requirements.txt`
  7. In `bot.py`, import your `credentials.py` file i.e `import credentials`, then change lines 9-12, thus:
  ```
  consumer_key = credentials.API_KEY
  consumer_secret_key = credentials.API_SECRET_KEY
  access_token = credentials.ACCESS_TOKEN
  access_token_secret = credentials.ACCESS_TOKEN_SECRET
  ```
  8. Save changes and run `bot.py`.
  9. To stop script at any point in time press `ctrl + c`.
  
  ## Deployment to Heroku
  You can follow the tutorial found [here](https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39)
  UPDATE:
  I wrote about it [here](https://medium.com/datadriveninvestor/making-a-quote-tweeting-twitter-bot-with-python-tweepy-and-heroku-69a11cd3f47e) also.
  
  ## Example Quotes
  1. I am a Khaleesi of the Dothraki. I am the wife of the great Kahl and I carry his son inside me. The next time you raise a hand to me will be the last time you have hands. 
            ~ Daenerys Targaryen
  2. "Oh, monster? Perhaps you should speak to me more softly then. Monsters are dangerous and just now Kings are dying like flies." 
            ~ Tyrion
  
  ## References
  1. [How to set up a twitter bot with Python and Heroku](https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39)
  2. [Build and Deploy Twitter Bots with Python, Tweepy and PythonAnywhere](https://www.twilio.com/blog/build-deploy-twitter-bots-python-tweepy-pythonanywhere)
  3. [Selecting Random Item From a List](https://pynative.com/python-random-choice/)
  4. [Deploying python applications with heroku](https://stackoverflow.com/a/50498116)
