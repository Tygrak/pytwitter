import tweepy
import pickle
import signal
import sys
import datetime

from streamListener import *
from tweetData import *

tweets = []
def signal_handler(sig, frame):
    print("\nExiting...")
    if len(tweets) > 1:
        output = open('data.pkl', 'wb')
        pickle.dump(tweets, output)
        output.close()
        print("Saved {0} tweets.".format(len(tweets)))
    sys.exit(0)
    
signal.signal(signal.SIGINT, signal_handler)

try:
    pickleFile = open('data.pkl', 'rb')
    tweets = pickle.load(pickleFile)
    pickleFile.close()
    print("Successfully loaded data from {0} tweets.".format(len(tweets)))
except:
    print("Couldn't load pickle file, starting new data list.")

with open("settings.txt", "r") as f:
    consumer_key = str.strip(f.readline())
    consumer_secret = str.strip(f.readline())
    access_token = str.strip(f.readline())
    access_token_secret = str.strip(f.readline())

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

words = []
with open("words.txt", "r") as wordsFile:
    while True:
        line = wordsFile.readline()
        if not line:
            break
        line = line.strip().split(" ")[0].strip()
        words.append(line)

streamListener = TwitterStreamListener(tweets)
sapi = tweepy.streaming.Stream(auth, streamListener)    
sapi.filter(track=words)