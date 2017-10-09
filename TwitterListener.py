import tweepy
import Transit

def getConsumerKey():
    file = open("keys.txt", "r")
    line = file.readline()
    consumerKey = line.rstrip("\n")

    line = file.readline()
    consumerSecret = line.rstrip("\n")

    line = file.readline()
    accessToken = line.rstrip("\n")

    line = file.readline()
    accessTokenSecret = line.rstrip("\n")
def toOrFrom(tweet):
    tweetList = tweet.split()
    transit = Transit.Transit()
    if "@buss_route" in tweetList:
        tweetList.remove("@buss_route")
    if tweetList[0][0] == "t" or tweetList[0][0] == "T":
        tweetString = "+".join(tweetList)
        tweetResponse = transit.getRouteTo(tweetString)
        return tweetResponse
    elif tweetList[0][0] == "F" or tweetList[0][0] == "f":
        tweetString = "+".join(tweetList)
        tweetResponse = transit.getRouteFrom(tweetString)
        return tweetResponse
    else:
        defaultTweet = "Please read the instructions and try again."
        return defaultTweet

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        id = status.user.screen_name
        text = status.text
        print(status.text)
        instructions = toOrFrom(text)
        message = "@" + id + " \n" + instructions
        print(message)
        if len(message) > 140:
            api.update_status(message[:140],in_reply_to_status_id = id)
            api.update_status(message[140:], in_reply_to_status_id=id)
        else:
            api.update_status(message, in_reply_to_status_id=id)

    def on_error(self, status_code):
        if status_code == 420:
            return False


file = open("keys.txt", "r")
line = file.readline()
consumerKey = line.rstrip("\n")

line = file.readline()
consumerSecret = line.rstrip("\n")

line = file.readline()
accessToken = line.rstrip("\n")

line = file.readline()
accessTokenSecret = line.rstrip("\n")
file.close()


auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.secure = True
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)