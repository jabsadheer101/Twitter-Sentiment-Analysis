import tweepy
from TextBlob import TextBlob

# firstly_authentication
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# secondly-retrieve_tweets_from_respective_keyword(s)
public_tweets = api.search('Ethiopia')


for tweet in public_tweets:
    print(tweet.text)
    
    # finally-perform_sentiment_analysis_on_tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
