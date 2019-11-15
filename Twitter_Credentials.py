import os
import tweepy
import json
#KEY-JSON
twitter_credentials= dict()
twitter_credentials['CONSUMER_KEY'] = 'F7P0Cg5I8SgOmmm0jiR2MEd8E'
twitter_credentials['CONSUMER_SECRET'] = 'aOC1wNicBbNbHx8VxVXkZ199ykyl8jiT8vqm4OUuds5SSvm9se'
twitter_credentials['ACCESS_TOKEN'] = '1169314161182068736-Rdw17TJQV3exntZfvoxRHN4QBPyctF'
twitter_credentials['ACCESS_SECRET'] = 'BhrPNuuBQ02dPZa3SpGPnz7P2LPfo65qhiL52MKBc4Bir'

with open('twitter_credentials.json', 'w') as twitter_info:
    json.dump(twitter_credentials, twitter_info, indent=4, sort_keys=True)