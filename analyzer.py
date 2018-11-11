import tweepy
import pickle
import datetime
import operator

from tweetData import *

def getLanguageCounts(tweets):
    languages = {}
    for i in range(len(tweets)):
        tweetLang = tweets[i].language
        if tweetLang in languages:
            languages[tweetLang] += 1
        else:
            languages[tweetLang] = 1

    return sorted(languages.items(), key=operator.itemgetter(1), reverse=True)

def getTimeCounts(tweets):
    times = dict.fromkeys(list(range(24)), 0)
    for i in range(len(tweets)):
        if tweets[i].time.day == 9:
            tweetTime = tweets[i].time
            times[tweetTime.hour] += 1

    return sorted(times.items(), key=operator.itemgetter(0))

def getSourceCounts(tweets):
    sources = {}
    for i in range(len(tweets)):
        tweetSource = tweets[i].source
        if tweetSource in sources:
            sources[tweetSource] += 1
        else:
            sources[tweetSource] = 1

    return sorted(sources.items(), key=operator.itemgetter(1), reverse=True)

def getPlaceCounts(tweets):
    places = {}
    for i in range(len(tweets)):
        if tweets[i].place:
            tweetPlace = str(tweets[i].place.country)
            if tweetPlace in places:
                places[tweetPlace] += 1
            else:
                places[tweetPlace] = 1

    return sorted(places.items(), key=operator.itemgetter(1), reverse=True)

def getWordCounts(tweets, words):
    words = dict.fromkeys(words, 0)
    for i in range(len(tweets)):
        for word in words:
            if word in tweets[i].text:
                words[word] += 1

    return sorted(words.items(), key=operator.itemgetter(1), reverse=True)