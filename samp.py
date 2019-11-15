import os
import tweepy
import json
import csv

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

#Scraping Tweets from User
name = input("Enter the twitter handle of the person whose tweets you want to download:- ")
all_the_tweets = []
count_tweet = 0
#name = 'elonmusk'
new_tweets = api.user_timeline(id=name, count=1)
all_the_tweets.extend(new_tweets)
oldest_tweet = all_the_tweets[-1].id - 1
while count_tweet < 3200:
    new_tweets = api.user_timeline(id=name, count=1, max_id=oldest_tweet)
    with open(str(name) + '_' + str(count_tweet) + '.json', 'a+') as json_file:
        #new_tweets['country'] = 'India'
        json.dump(new_tweets, json_file, indent=4)
    all_the_tweets.extend(new_tweets)
    oldest_tweet = all_the_tweets[-1].id - 1
    count_tweet = count_tweet + 1
    print ('...%s tweets have been downloaded so far' % len(all_the_tweets))

............................................................................
hash_tweets = []
count = 0
query= '#HillaryClinton' or '#Hillary' or '#Clinton' or '#hillaryclinton' or '#hillary' or '#clinton' or 'Hillary Clinton' or 'Hillary' or 'Clinton'
for hash_tweet in tweepy.Cursor(api.search, q=query, lang='en').items(1500):
    json_object = hash_tweet._json
    if 'retweeted_status' in json_object:
        pass
    else:
        hash_tweets.append(hash_tweet)
        with open(str(name) + '_hashtag_' + str(count) + '.json', 'a+', encoding='utf8') as json_file:
            json.dump(json_object, json_file, indent=4, ensure_ascii=False)
            print('...%s tweets have been downloaded so far' % len(hash_tweets))
            count = count + 1
            ..........................................................................................

