import tweepy
import pickle
import datetime
import operator
import matplotlib.pyplot as plt
import pycountry

from tweetData import *
from analyzer import *
from plotter import *

tweets = []

try:
    pickleFile = open('dataAll.pkl', 'rb')
    tweets = pickle.load(pickleFile)
    pickleFile.close()
    print("Successfully loaded data from {0} tweets.".format(len(tweets)))
except:
    print("Couldn't load pickle file, starting new data list.")

def plotEmojiFlagUsage():
    words = {}
    with open("words.txt", "r") as wordsFile:
        while True:
            line = wordsFile.readline()
            if not line:
                break
            line = line.strip().split(" ", 1)
            words[line[0].strip()] = line[1].strip().replace("Flag: ", "")

    flags = getWordCounts(tweets, words.keys())
    #flags = flags[:10]

    values = []
    labels = []
    i = 0
    for val in flags:
        i += 1
        #print("{3}. {0} ({1}) :: {2}".format(val[0], words[val[0]], val[1], i))
        print("{2}. {0} :: {1}".format(words[val[0]], val[1], i))
        label = "{0}. {1}".format(i, words[val[0]])
        labels.append(label)
        values.append(val[1])

    plotBarValues(labels, values, "Ten most used flag emojis", "Flag Emoji", "Amount of tweets")
    plt.show()

def plotLanguageUsage():
    langs = getLanguageCounts(tweets)
    langs = langs[:10]
    values = []
    labels = []
    i = 0
    for val in langs:
        i += 1
        langName = pycountry.languages.get(alpha_2=val[0]).name
        print("{2}. {0} :: {1}".format(langName, val[1], i))
        labels.append(langName)
        values.append(val[1])
    plotBarValues(labels, values, "Ten most used languages in tweets", "Language", "Amount of tweets")
    plt.show()

def plotPlaceUsage():
    places = getPlaceCounts(tweets)
    places = places[:10]
    values = []
    labels = []
    for val in places:
        print("{0} :: {1}".format(val[0], val[1]))
        labels.append(val[0])
        values.append(val[1])
    plotBarValues(labels, values, "Twitter usage by place", "Place", "Amount of tweets")
    plt.show()

def plotTimeUsage():
    times = getTimeCounts(tweets)
    values = []
    labels = []
    for val in times:
        print("{0} :: {1}".format(val[0], val[1]))
        labels.append(val[0])
        values.append(val[1])
    plotBarValues(labels, values, "Twitter usage by time", "Time", "Amount of tweets")
    plt.show()

def plotSourceUsage():
    sources = getSourceCounts(tweets)
    sources = sources[:5]
    values = []
    labels = []
    for val in sources:
        print("{0} :: {1}".format(val[0], val[1]))
        labels.append(val[0])
        values.append(val[1])
    plotBarValues(labels, values, "Twitter usage by source", "Source", "Amount of tweets")
    plt.show()

#plotLanguageUsage()
plotEmojiFlagUsage()
#plotTimeUsage()
#plotSourceUsage()
#plotPlaceUsage()