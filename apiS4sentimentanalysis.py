from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import SentimentOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Example Text for Sentiment Analysis
text = "Anmol is good but ars is best"

# TextBlob
def analyze_with_textblob(text):
    analysis = TextBlob(text)
    sentiment = "positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"
    return sentiment

# VADER
def analyze_with_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    sentiment = "positive" if sentiment_scores['compound'] > 0 else "negative" if sentiment_scores['compound'] < 0 else "neutral"
    return sentiment

# IBM Watson Natural Language Understanding
def analyze_with_ibm_watson(text):
    api_key = "YOUR_IBM_API_KEY"
    url = "YOUR_IBM_URL"
    authenticator = IAMAuthenticator(api_key)
    nlu = NaturalLanguageUnderstandingV1(version="2021-08-01", authenticator=authenticator)
    nlu.set_service_url(url)

    response = nlu.analyze(text=text, features=SentimentOptions()).get_result()
    sentiment = response["sentiment"]["document"]["label"]
    return sentiment

# Microsoft Azure Text Analytics
def analyze_with_azure(text):
    api_key = "YOUR_AZURE_API_KEY"
    endpoint = "YOUR_AZURE_ENDPOINT"
    credential = AzureKeyCredential(api_key)
    client = TextAnalyticsClient(endpoint, credential)

    response = client.analyze_sentiment(documents=[text])[0]
    sentiment = response.sentiment
    return sentiment

# Using the functions
textblob_sentiment = analyze_with_textblob(text)
vader_sentiment = analyze_with_vader(text)
ibm_watson_sentiment = analyze_with_ibm_watson(text)
azure_sentiment = analyze_with_azure(text)

print("TextBlob Sentiment:", textblob_sentiment)
print("VADER Sentiment:", vader_sentiment)
print("IBM Watson Sentiment:", ibm_watson_sentiment)
print("Azure Sentiment:", azure_sentiment)
  
