import os
import json
import emoji
import re
import codecs
from datetime import datetime

def getHashtags(json_file_name):
    hashtags = []
    with open(json_file_name, encoding="utf8") as json_data:
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
    with open(json_file_name, encoding="utf8") as json_data:
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
    with open(json_file_name, encoding="utf8") as json_data:
        data_dict = json.load(json_data)
        string = data_dict['text']
        for c in string:
            if c in emoji.UNICODE_EMOJI:
                emojis.append(c)
    return emojis

def getURLs(json_file_name):
    urls = []
    with open(json_file_name, encoding="utf8") as json_data:
        data_dict = json.load(json_data)
        string = data_dict['text']
        return re.findall(r'(https?://[^\s]+)', string)

def getFormattedTweetText(json_file_name,stopwords,emojis):
    with open(json_file_name, encoding="utf8") as json_data:
        data_dict = json.load(json_data)
        dataObj = datetime.strptime(data_dict['created_at'],'%a %b %d %H:%M:%S %z %Y').strftime("%Y-%m-%dT%H:%M:%SZ")
        print(str(dataObj))
        print(type(dataObj))

        string = data_dict['text']
        string_without_emojis = ''.join([c for c in string if c not in emojis])
        print("STRING WITHOUT EMOJIS : "+string_without_emojis)
        query_words = string_without_emojis.split()
        result_words = [word for word in query_words if word not in stopwords]
        result = ' '.join(result_words)
    return result

def getFormattedDate(json_file_name):
    with open(json_file_name, encoding="utf8") as json_data:
        data_dict = json.load(json_data)
        dataObj = datetime.strptime(data_dict['created_at'],'%a %b %d %H:%M:%S %z %Y').strftime("%Y-%m-%dT%H:%M:%SZ")
        print(str(dataObj))
        print(type(dataObj))
    return str(dataObj)

def updateJSON(json_file_name,dictionary):
    input_file  = open(json_file_name, "r", encoding="utf8")
    j = json.loads(input_file.read())
    output_file = codecs.open(json_file_name, "w", encoding="utf-8")
    j['tweet_urls'] = dictionary['urls']
    j['mentions'] = dictionary['mentions']
    j['tweet_emoticons'] = dictionary['emojis']
    j['hashtags'] = dictionary['hashtags']
    j['formatted_text'] = dictionary['formatted_text']
    j['created_at'] = dictionary['formatted_date']
    json.dump(j, output_file, indent=4, ensure_ascii=False)

def preprocessData(json_file_name):
    print(json_file_name)
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
    formatted_date = getFormattedDate(json_file_name)
    preprocessData_dictionary['hashtags'] = hashtags
    preprocessData_dictionary['mentions'] = mentions
    preprocessData_dictionary['urls'] = urls
    preprocessData_dictionary['emojis'] = emojis
    preprocessData_dictionary['formatted_text'] = formatted_text
    preprocessData_dictionary['formatted_date'] = formatted_date
    print(preprocessData_dictionary)
    updateJSON(json_file_name,preprocessData_dictionary)

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

print(os.listdir())
def start():
    folders = ['USA','Brazil','India']
    usa_politicians = ['Hillary Clinton','Mike Pence','Kamala Harris','Joe Biden','Elizabeth Warren']
    brazil_politicians = ['Zeca Dirceu','Alexandre Garcia','Carlos Bolsonaro','Eduardo Bolsonaro','Jair M. Bolsonaro']
    india_politicians = ['Yogi Adityanath','AmitShah','Rajnath Singh','Jyotiraditya M. Scindia','Narendra Modi']
    #listOfFiles = getListOfFiles('C:\\Users\\Kapindran\\Project1\\USA\\realDonaldTrump')
    file_count = 0
    json_count = 0
    tweet_count = 0
    # for x in usa_politicians :
    #     listOfFiles = getListOfFiles('C:/Users/Kapindran/Project1/USA/'+x)
    #     tweet_count += len(listOfFiles)
    #     print("Retrieved "+str(len(listOfFiles))+" tweets from "+x)
    #     for i in listOfFiles :
    #         if i.endswith('.json') :
    #             json_count += 1
    #             preprocessData(i)
    # print("Totally processed "+str(json_count)+"JSONS")

    # for x in brazil_politicians :
    #     listOfFiles = getListOfFiles('C:/Users/Kapindran/Project1/Brazil/'+x)
    #     tweet_count += len(listOfFiles)
    #     print("Retrieved "+str(len(listOfFiles))+" tweets from "+x)
    #     for i in listOfFiles :
    #         if i.endswith('.json') :
    #             json_count += 1
    #             preprocessData(i)
    # print("Totally processed "+str(json_count)+"JSONS")

    #for x in india_politicians :
    listOfFiles = getListOfFiles('C:/Users/Kapindran/Project1/HASHTAGS/')
    tweet_count += len(listOfFiles)
        #print("Retrieved "+str(len(listOfFiles))+" tweets from "+x)
    for i in listOfFiles :
        if i.endswith('.json') :
            json_count += 1
            preprocessData(i)
    print("Totally processed "+str(json_count)+"JSONS")


if __name__ == "__main__":
    start() # Keep the file in same directory and try for a different JSON
