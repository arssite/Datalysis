#TextBlob or VADER (Valence Aware Dictionary and sEntiment Reasoner)


#template for textBlob is here
import tweepy
from textblob import TextBlob
import tkinter as tk
from tkinter import messagebox

# Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Set up Tweepy authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to analyze sentiment
def analyze_sentiment(username):
    try:
        tweets = api.user_timeline(screen_name=username, count=10)
        positive = 0
        neutral = 0
        negative = 0

        for tweet in tweets:
            analysis = TextBlob(tweet.text)
            if analysis.sentiment.polarity > 0:
                positive += 1
            elif analysis.sentiment.polarity < 0:
                negative += 1
            else:
                neutral += 1

        total_tweets = len(tweets)
        positive_percentage = (positive / total_tweets) * 100
        neutral_percentage = (neutral / total_tweets) * 100
        negative_percentage = (negative / total_tweets) * 100

        result = f"Positive: {positive_percentage:.2f}%\nNeutral: {neutral_percentage:.2f}%\nNegative: {negative_percentage:.2f}%"
        return result

    except tweepy.TweepError as e:
        return str(e)

# UI setup
def get_sentiment():
    username = username_entry.get()
    sentiment_result = analyze_sentiment(username)
    messagebox.showinfo("Sentiment Analysis Result", sentiment_result)

root = tk.Tk()
root.title("Twitter Sentiment Analysis")

username_label = tk.Label(root, text="Enter Twitter Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

analyze_button = tk.Button(root, text="Analyze Sentiment", command=get_sentiment)
analyze_button.pack()

root.mainloop()



#how to fetch api
'''To access the Twitter API and retrieve tweets for sentiment analysis using Tweepy, follow these steps:

Create a Twitter Developer Account:
If you don't have a Twitter Developer account, go to the Twitter Developer Platform and create an account.

Create a Twitter App:
Once you have a developer account, log in to the Twitter Developer Dashboard and create a new app. Fill in the required information, and you'll be provided with API keys and access tokens.

Get API Keys and Access Tokens:
After creating the app, navigate to the "Keys and tokens" tab. Here, you'll find your Consumer Key (API Key), Consumer Secret (API Secret Key), Access Token, and Access Token Secret.

Install Tweepy and TextBlob:  pip install tweepy textblob

Use the Code bro'''
