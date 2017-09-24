import tweepy

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
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        id = status.user.screen_name
        text = status.text
        print(status.text)
        message = "@" + id + " Hello !"
        print(message)
        api.update_status(message,in_reply_to_status_id = id)

    def on_error(self, status_code):
        if status_code == 420:
            return False


consumerKey = ""
consumerSecret = ""
accessToken = ""
accessTokenSecret = ""

getConsumerKey()

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.secure = True
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)