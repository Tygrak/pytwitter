import tweepy
import pickle
import datetime
import operator
import matplotlib.pyplot as plt
import pycountry

from tweetData import *
from analyzer import *
from plotting import *
from plotHelper import *

tweets = []

try:
    pickleFile = open('dataAll.pkl', 'rb')
    tweets = pickle.load(pickleFile)
    pickleFile.close()
    print("Successfully loaded data from {0} tweets.".format(len(tweets)))
except:
    print("Couldn't load pickle file, starting new data list.")

#plotLanguageUsage(tweets)
#plotEmojiFlagUsage(tweets)
plotEmojiFlagUsageNormalized(tweets)
#plotTimeUsage(tweets)
#plotSourceUsage(tweets)
#plotPlaceUsage(tweets)