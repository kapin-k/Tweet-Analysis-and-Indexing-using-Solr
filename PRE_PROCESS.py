import json
class PreprocessTweets:


    def preprocessForUser(self,user):
         path = "C:/Users/Kapindran/Project1/TWEET_JSON/" + user + ".json"

         with open(path) as json_file:
              tweets = json.load(json_file)

    def fetchSeperateFields(self, tweets, tweetFileName):
        for tweet in tweets:
        # hashTags = re.findall(r"#(\w+)", tweet['text'])
        # print(tweet['text'])
        # print(hashTags)

            hashTagsFiltered = self.hashtags123(tweet)
            hashTagModified = []
            for hashTG in hashTagsFiltered:
                hashTG = re.sub('[#]', '', hashTG)
                hashTagModified.append(hashTG)

            print(tweet['text'])

            print('hashtags')
            print(hashTagModified)
            tweet['hashtags'] = hashTagModified

            mentionsFiltered = self.filterMentions(tweet)
            print('mentions')
            print(mentionsFiltered)
            tweet['mentions'] = mentionsFiltered

            URLSFiltered = self.filterURLs(tweet)
            print('Urls')
            print(URLSFiltered)
            tweet['tweet_urls'] = URLSFiltered

            emojis_filtered = self.extract_emojis(tweet)
            if len(emojis_filtered) > 0:
                self.filewithEmoticons = tweetFileName
            print('emoji filterd')
            print(emojis_filtered)
            tweet['tweet_emoticons'] = emojis_filtered
            print("******************************************")

            tweet['tweet_date'] = self.getFormattedDate(tweet)

            self.modifyPOIname_POIid_replyText_tweetText(tweet)
        return tweets


    def hashtags123(self, tweet):
        return list(filter(lambda token: token.startswith('#'), tweet['text'].split()))


    def filterMentions(self, tweet):
        text = re.sub("[\w]+@[\w]+\.[c][o][m]", "", tweet['text'])
        result = re.findall("@([a-zA-Z0-9]{1,15})", text)
        return result


    def filterURLs(self, tweet):
        result = re.findall(r'(https?://[^\s]+)', tweet['text'])
        return result


    def extract_emojis(self, tweet):
        return [c for c in tweet['text'] if c in emoji.UNICODE_EMOJI]


    def getFormattedDate(self, tweet):
        print(tweet['created_at'])
        dataObj = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S %z %Y')
        dataObj = dataObj.replace(minute=0, second=0)
        print(dataObj.strftime("%Y-%m-%dT%H:%M:%SZ"))
        return dataObj.strftime("%Y-%m-%dT%H:%M:%SZ")


    def modifyPOIname_POIid_replyText_tweetText(self, tweet):
        print(tweet['text'])
        tweet['tweet_text'] = tweet['text']
        tweet['tweet_lang'] = tweet['lang']
        if not tweet['in_reply_to_status_id'] is None:
            tweet['reply_text'] = tweet['text']
            tweet['replied_to_tweet_id'] = tweet['in_reply_to_status_id']
            tweet['replied_to_user_id'] = tweet['in_reply_to_user_id']
            tweet['poi_id'] = tweet['in_reply_to_user_id']
            tweet['poi_name'] = tweet['in_reply_to_screen_name']
        else:
            tweet['tweet_text'] = tweet['text']
            tweet['reply_text'] = None
            tweet['replied_to_tweet_id'] = None
            tweet['replied_to_user_id'] = None
            tweet['poi_id'] = tweet['user']['id']
            tweet['poi_name'] = tweet['user']['screen_name']



if __name__ == "__main__":
    pp = PreprocessTweets()
    pp.preprocessForUser("alexandregarcia")