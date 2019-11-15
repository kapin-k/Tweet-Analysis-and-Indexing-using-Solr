import os
import tweepy
import json

#OAuth Handler Instance and Authentication

with open('twitter_credentials.json') as twitter_json:
    secret = json.load(twitter_json)
C_KEY = secret['CONSUMER_KEY']
C_SECRET = secret['CONSUMER_SECRET']
A_TOKEN = secret['ACCESS_TOKEN']
A_SECRET = secret['ACCESS_SECRET']

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_SECRET)
api = tweepy.API(auth)
#api = tweepy.API(auth, wait_on_rate_limit=True)

#TweetScraping

#name = input("Enter the twitter handle of the person whose tweets you want to download:- ")
name = 'zeca_dirceu'
# tweets = []
# for tweet in tweepy.Cursor(api.user_timeline, id=name).items(3200):
#     json_object = tweet._json
#     with open(str(name) + '_' + str(len(tweets)) + '.json', 'a+', encoding='utf8') as json_file:
#         if 'retweeted_status' in json_object:
#            pass
#         elif json_object['in_reply_to_status_id']:
#             pass
#         else:
#             json_object['country'] = 'USA'
#             tweets.append(tweet)
#             json.dump(json_object, json_file, indent=4, ensure_ascii=False)
#             print('...%s tweets have been downloaded so far' % len(tweets))
#
# with open(str(name) + '.json', 'w', encoding='utf8') as json_file:
#     for status in tweets:
#        JSON_OBJECTS = status._json
#        json.dump(JSON_OBJECTS, json_file, indent=4, ensure_ascii=False)

#Hashtag and Keyword Retrievals

hash_tweets = []
count = 1855
query= '#zeca_dirceu' or '#Zeca' or '#Dirceu' or '#Zeca_Dirceu' or '#tchutchuca' or '#Brazil' or 'Brazil Zeca Dirceu' or 'Zeca Dirceu'
for hash_tweet in tweepy.Cursor(api.search, q=query, lang='en').items(1000):
   json_object = hash_tweet._json
   if 'retweeted_status' in json_object:
       pass
   else:
       hash_tweets.append(hash_tweet)
       with open(str(name) + '_hashtag_' + str(count) + '.json', 'a+', encoding='utf8') as json_file:
           json.dump(json_object, json_file, indent=4, ensure_ascii=False)
           print('...%s tweets have been downloaded so far' % str(count))
           count = count + 1

 # def replies(self, tweet, recursive=False, prune=()):
 #        """
 #        replies returns a generator of tweets that are replies for a given
 #        tweet. It includes the original tweet. If you would like to fetch the
 #        replies to the replies use recursive=True which will do a depth-first
 #        recursive walk of the replies. It also walk up the reply chain if you
 #        supply a tweet that is itself a reply to another tweet. You can
 #        optionally supply a tuple of tweet ids to ignore during this traversal
 #        using the prune parameter.
 #        """
 #
 #        yield tweet
 #
 #        # get replies to the tweet
 #        screen_name = tweet['user']['screen_name']
 #        tweet_id = tweet['id_str']
 #        log.info("looking for replies to: %s", tweet_id)
 #        for reply in self.search("to:%s" % screen_name, since_id=tweet_id):
 #
 #            if reply['in_reply_to_status_id_str'] != tweet_id:
 #                continue
 #
 #            if reply['id_str'] in prune:
 #                log.info("ignoring pruned tweet id %s", reply['id_str'])
 #                continue
 #
 #            log.info("found reply: %s", reply["id_str"])
 #
 #            if recursive:
 #                if reply['id_str'] not in prune:
 #                    prune = prune + (tweet_id,)
 #                    for r in self.replies(reply, recursive, prune):
 #                        yield r
 #            else:
 #                yield reply
 #
 #        # if this tweet is itself a reply to another tweet get it and
 #        # get other potential replies to it
 #
 #        reply_to_id = tweet.get('in_reply_to_status_id_str')
 #        log.info("prune=%s", prune)
 #        if recursive and reply_to_id and reply_to_id not in prune:
 #            t = self.tweet(reply_to_id)
 #            if t:
 #                log.info("found reply-to: %s", t['id_str'])
 #                prune = prune + (tweet['id_str'],)
 #                for r in self.replies(t, recursive=True, prune=prune):
 #                    yield r
 #
 #        # if this tweet is a quote go get that too whatever tweets it
 #        # may be in reply to
 #
 #        quote_id = tweet.get('quotes_status_id_str')
 #        if recursive and quote_id and quote_id not in prune:
 #            t = self.tweet(quote_id)
 #            if t:
 #                log.info("found quote: %s", t['id_str'])
 #                prune = prune + (tweet['id_str'],)
 #                for r in self.replies(t, recursive=True, prune=prune):
 #                    yield r