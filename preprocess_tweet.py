import json
import emoji
import re
import codecs

def getHashtags(json_file_name):
    hashtags = []
    with open(json_file_name) as json_data:
        data_dict = json.load(json_data)
        length_of_hashtags = len(data_dict['entities']['hashtags'])
        if length_of_hashtags > 0 :
            for i in range(0,length_of_hashtags):
                hashtags.append(data_dict['entities']['hashtags'][i]['text'])
            return hashtags
        else :
            return None

def getMentions(json_file_name):
    mentions = []
    with open(json_file_name) as json_data:
        data_dict = json.load(json_data)
        length_of_mentions = len(data_dict['entities']['user_mentions'])
        if length_of_mentions > 0 :
            for i in range(0,length_of_mentions):
                mentions.append(data_dict['entities']['user_mentions'][i]['screen_name'])
            return mentions
        else :
            return None

def getEmojis(json_file_name):
    emojis = []
    with open(json_file_name) as json_data:
        data_dict = json.load(json_data)
        string = data_dict['text']
        for c in string:
            if c in emoji.UNICODE_EMOJI:
                emojis.append(c)
    return emojis

def getURLs(json_file_name):
    urls = []
    with open(json_file_name) as json_data:
        data_dict = json.load(json_data)
        string = data_dict['text']
        return re.findall(r'(https?://[^\s]+)', string)

def getFormattedTweetText(json_file_name,stopwords,emojis):
    with open(json_file_name) as json_data:
        data_dict = json.load(json_data)
        string = data_dict['text']
        string_without_emojis = ''.join([c for c in string if c not in emojis])
        print("STRING WITHOUT EMOJIS : "+string_without_emojis)
        query_words = string_without_emojis.split()
        result_words = [word for word in query_words if word not in stopwords]
        result = ' '.join(result_words)
    return result

def updateJSON(json_file_name,dictionary):
    input_file  = open(json_file_name, "r")
    j = json.loads(input_file.read())
    output_file = codecs.open(json_file_name, "w", encoding="utf-8")
    j['tweet_urls'] = dictionary['urls']
    j['mentions'] = dictionary['mentions']
    j['tweet_emoticons'] = dictionary['emojis']
    j['hashtags'] = dictionary['hashtags']
    j['formatted_text'] = dictionary['formatted_text']
    json.dump(j, output_file, indent=4, ensure_ascii=False)

def preprocessData(json_file_name):
    preprocessData_dictionary = {}
    mentions_with_at = []
    hashtags_with_hash = []
    hashtags = getHashtags(json_file_name)
    mentions = getMentions(json_file_name)
    emojis = getEmojis(json_file_name)
    urls = getURLs(json_file_name)
    if mentions is not None:
        mentions_with_at = ["@" + i for i in mentions]
    if hashtags is not None:
        hashtags_with_hash = ["#" + i for i in hashtags]
    stopwords = hashtags_with_hash + mentions_with_at + urls
    formatted_text = getFormattedTweetText(json_file_name,stopwords,emojis)
    preprocessData_dictionary['hashtags'] = hashtags
    preprocessData_dictionary['mentions'] = mentions
    preprocessData_dictionary['urls'] = urls
    preprocessData_dictionary['emojis'] = emojis
    preprocessData_dictionary['formatted_text'] = formatted_text
    print(preprocessData_dictionary)
    updateJSON(json_file_name,preprocessData_dictionary)

if __name__ == "__main__":
    preprocessData('hashtag.json') # Keep the file in same directory and try for a different JSON
