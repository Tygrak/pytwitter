import tweepy
import pickle
import datetime
import operator
import matplotlib.pyplot as plt
import pycountry

from tweetData import *
from analyzer import *
from plotHelper import *

def plotEmojiFlagUsage(tweets):
    words = {}
    with open("words.txt", "r") as wordsFile:
        while True:
            line = wordsFile.readline()
            if not line:
                break
            line = line.strip().split(" ", 1)
            words[line[0].strip()] = line[1].strip().replace("Flag: ", "")

    flags = getWordCounts(tweets, words.keys())
    flags = flags[:10]

    values = []
    labels = []
    i = 0
    for val in flags:
        i += 1
        print("{2}. {0} :: {1}".format(words[val[0]], val[1], i))
        label = "{0}. {1}".format(i, words[val[0]])
        labels.append(label)
        values.append(val[1])

    plotBarValues(labels, values, "Ten most used flag emojis", "Flag Emoji", "Amount of tweets")
    plt.show()

def plotEmojiFlagUsageNormalized(tweets):
    words = {}
    with open("words.txt", "r") as wordsFile:
        while True:
            line = wordsFile.readline()
            if not line:
                break
            line = line.strip().split(" ", 1)
            words[line[0].strip()] = line[1].strip().replace("Flag: ", "")
    
    populations = {}
    with open("countryPopulation.csv", "r") as wordsFile:
        while True:
            line = wordsFile.readline()
            if not line:
                break
            line = line.strip().split(",")
            if len(line) >= 62:
                num = line[62].strip('"')
                if num.isdigit():
                    populations[line[0].strip('"')] = int(num)

    flags = getWordCounts(tweets, words.keys())
    for i in range(len(flags)):
        if words[flags[i][0]] in populations and populations[words[flags[i][0]]] > 250000:
            flags[i] = (flags[i][0], flags[i][1]/populations[words[flags[i][0]]])
        else:
            flags[i] = (flags[i][0], -1)
            
    flags = sorted(flags, key=lambda x: x[1], reverse=True)
    flags = flags[:200]
    flags = [(x[0], x[1]/max(flags, key=lambda x: x[1])[1]) for x in flags]

    values = []
    labels = []
    i = 0
    for val in flags:
        i += 1
        print("{2}. {0} :: {1}".format(words[val[0]], val[1], i))
        label = "{0}. {1}".format(i, words[val[0]])
        labels.append(label)
        values.append(val[1])

    plotBarValues(labels, values, "Ten most popular countries (twitter usage/population)", "Flag Emoji", "Amount of tweets")
    plt.show()

def plotLanguageUsage(tweets):
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

def plotPlaceUsage(tweets):
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

def plotTimeUsage(tweets):
    times = getTimeCounts(tweets)
    values = []
    labels = []
    for val in times:
        print("{0} :: {1}".format(val[0], val[1]))
        labels.append(val[0])
        values.append(val[1])
    plotBarValues(labels, values, "Twitter usage by time", "Time", "Amount of tweets")
    plt.show()

def plotSourceUsage(tweets):
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