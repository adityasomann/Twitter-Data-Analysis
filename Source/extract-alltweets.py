import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener 


consumer_key = 'Niz0CCufq3NwzHXFrcuq1i3Mf'
consumer_secret = 'QthX3LcN0HgnYUvqk9xU4FHJdOkPaz7dvTDcbyPfn6y5ydtU3Q'
access_token = '474841905-QMMIBJlfczzEIbkhmgrlZCGafeBGGZ78cxnZfMtp'
access_secret = 'sfr0nenrpCfWvqacBiExkV8hYsAC81QgJsNl31dslQp9v'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        print(data)
	newFile = open('twitter2tweets.txt','a')
	newFile.write(data)
	newFile.write('\n')
	newFile.close()  
       	return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['Policitics'])


		
