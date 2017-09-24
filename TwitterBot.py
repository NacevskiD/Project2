import tweepy
import TwitterListener


myStreamListener = TwitterListener.MyStreamListener()
myStream = tweepy.Stream(auth = TwitterListener.api.auth,listener= myStreamListener)
myStream.filter(track=["@buss_route"])

