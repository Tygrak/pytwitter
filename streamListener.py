import tweepy
import datetime
import pickle

from tweetData import *

class TwitterStreamListener(tweepy.StreamListener):
    def __init__(self, tweetDataList):
        tweepy.StreamListener.__init__(self)
        self.receivedTweets = 0
        self.timeStarted = datetime.datetime.now()
        self.lastBatchTime = datetime.datetime.now()
        self.tweetDataList = tweetDataList

    def on_status(self, status):
        newTweet = tweetData(status.created_at, status.text, status.user.lang, 
            status.user.time_zone, status.user.location, status.coordinates, 
            status.place, status.user.followers_count, status.user.screen_name, 
            status.user.name, status.source)
        self.tweetDataList.append(newTweet)
        self.receivedTweets += 1
        if self.receivedTweets%500 == 0:
            output = open('data.pkl', 'wb')
            pickle.dump(self.tweetDataList, output)
            output.close()
            batchSeconds = (datetime.datetime.now() - self.lastBatchTime).total_seconds()
            self.lastBatchTime = datetime.datetime.now()
            print("{0}: {1} tweets received, last batch took {2} seconds.".format(datetime.datetime.now(), self.receivedTweets, batchSeconds))


    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream