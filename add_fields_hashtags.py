import os
import json
import emoji
import re
import codecs
from datetime import datetime
import string


def preprocessData(json_file_name):
    id_dictionary = {'HillaryClinton':1339835893,
        'AmitShah':1447949844,
        'narendramodi':18839785,
        'rajnathsingh':1346439824,
        'myogiadityanath':3437532637,
        'SenWarren':970207298,
        'JoeBiden':939091,
        'KamalaHarris':30354991,
        'mike_pence':22203756,
        'jairbolsonaro':128372940
        }
    input_file  = open(json_file_name, "r", encoding="utf8")
    file_name_array = json_file_name.split('/')
    file_name = file_name_array[len(file_name_array) - 1]
    screen_name = file_name.split('_')[0]
    if screen_name=='mike':
        screen_name='mike_pence'
    j = json.loads(input_file.read())
    j['poi_name'] = screen_name
    j['poi_id'] = id_dictionary[screen_name]
    j['replied_to_tweet_id'] = None
    j['replied_to_user_id'] = None
    j['reply_text'] = None
    j['verified'] = j['user']['verified']
    j['tweet_text'] = j['text']
    lang = j['lang']
    j['tweet_lang'] = lang
    try :
        if lang in ['en','hi','pt'] :
            j['tweet_'+str(lang)] = getStringWithoutPunctuation(j['formatted_text'])
        else :
            if j['poi_name'] in ['HillaryClinton','SenWarren','JoeBiden','KamalaHarris','mike_pence']:
                j['tweet_en'] = getStringWithoutPunctuation(j['formatted_text'])
                j['tweet_lang'] = 'en'
                print("Changed language to English :- "+json_file_name)
            elif j['poi_name'] in ['zeca_dirceu','alexandregarcia','CarlosBolsonaro','BolsonaroSP','jairbolsonaro']:
                j['tweet_pt'] = getStringWithoutPunctuation(j['formatted_text'])
                j['tweet_lang'] = 'pt'
                print("Changed language to Portugese :- "+json_file_name)
            elif j['poi_name'] in ['AmitShah','rajnathsingh','JM_Scindia','narendramodi','myogiadityanath']:
                j['tweet_hi'] = getStringWithoutPunctuation(j['formatted_text'])
                j['tweet_lang'] = 'hi'
                print("Changed language to Hindi :- "+json_file_name)
            else :
                print("EMERGENCY CHECK THIS FILE :- "+json_file_name)
        j['tweet_date'] = j['created_at']
        output_file = codecs.open(json_file_name, "w", encoding="utf-8")
        json.dump(j, output_file, indent=4, ensure_ascii=False)
    except KeyError:
        os.remove(json_file_name)
        print("**************Removing file  "+json_file_name+"**************")

    if False :
        j = json.loads(input_file.read())
        j['poi_name'] = j['user']['screen_name']
        j['poi_id'] = j['user']['id']
        j['replied_to_tweet_id'] = j['in_reply_to_status_id']
        j['replied_to_user_id'] = j['in_reply_to_user_id']
        if j['replied_to_tweet_id'] is None:
            j['reply_text'] = None
        j['verified'] = j['user']['verified']
        j['tweet_text'] = j['text']
        lang = j['lang']
        j['tweet_lang'] = lang
        if lang in ['en','hi','pt','es'] :
            j['tweet_'+str(lang)] = getStringWithoutPunctuation(j['formatted_text'])
        else :
            if 'tweet_xx' in j:
                del j['tweet_xx']
            if j['poi_name'] in ['HillaryClinton','SenWarren','JoeBiden','KamalaHarris','mike_pence']:
                j['tweet_en'] = getStringWithoutPunctuation(j['formatted_text'])
                j['tweet_lang'] = 'en'
                print("Changed language to English :- "+json_file_name)
            elif j['poi_name'] in ['zeca_dirceu','alexandregarcia','CarlosBolsonaro','BolsonaroSP','jairbolsonaro']:
                j['tweet_pt'] = getStringWithoutPunctuation(j['formatted_text'])
                j['tweet_lang'] = 'pt'
                print("Changed language to Portugese :- "+json_file_name)
            elif j['poi_name'] in ['AmitShah','rajnathsingh','JM_Scindia','narendramodi','myogiadityanath']:
                j['tweet_hi'] = getStringWithoutPunctuation(j['formatted_text'])
                j['tweet_lang'] = 'hi'
                print("Changed language to Hindi :- "+json_file_name)
            else :
                print("EMERGENCY CHECK THIS FILE :- "+json_file_name)
        j['tweet_date'] = j['created_at']
        output_file = codecs.open(json_file_name, "w", encoding="utf-8")
        json.dump(j, output_file, indent=4, ensure_ascii=False)

def getStringWithoutPunctuation(sentence):
    if sentence != None:
        result_string = ' '.join(word.strip(string.punctuation) for word in sentence.split())
        result_string = re.sub(' +', ' ',result_string)
        return result_string
    else:
        return ''

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

def start():
    folders = ['USA','Brazil','India']
    usa_politicians = ['Hillary Clinton', 'Mike Pence', 'Kamala Harris', 'Joe Biden', 'Elizabeth Warren']
    brazil_politicians = ['Zeca Dirceu', 'Alexandre Garcia', 'Carlos Bolsonaro', 'Eduardo Bolsonaro', 'Jair M. Bolsonaro']
    india_politicians = ['Yogi Adityanath', 'AmitShah', 'Rajnath Singh', 'Jyotiraditya M. Scindia', 'Narendra Modi']
    file_count = 0
    json_count = 0
    # for x in usa_politicians :
    #     listOfFiles = getListOfFiles('/Users/latheesh/Documents/Dry_Run/Final_Data_copy/Hashtags_and_Keywords/USA/'+x)
    #     for i in listOfFiles :
    #         if i.endswith('.json') :
    #             json_count += 1
    #             preprocessData(i)
    # for x in india_politicians :
    #     listOfFiles = getListOfFiles('/Users/latheesh/Documents/Dry_Run/Final_Data_copy/Hashtags_and_Keywords/India/'+x)
    #     json_count += len(listOfFiles)
    #     for i in listOfFiles :
    #         if i.endswith('.json') :
    #             json_count += 1
    #             preprocessData(i)

    #for x in brazil_politicians :
    #     listOfFiles = getListOfFiles('/Users/latheesh/Documents/Dry_Run/Final_Data_copy/Hashtags_and_Keywords/Brazil/'+x)
    #     json_count += len(listOfFiles)
    #     for i in listOfFiles :
    #         if i.endswith('.json') :
    #             json_count += 1
    #             preprocessData(i)
    # print("Totally processed "+str(json_count)+" JSONS")

    listOfFiles = getListOfFiles('C:/Users/Kapindran/Project1/HASHTAGS/')
    json_count += len(listOfFiles)
        #print("Retrieved "+str(len(listOfFiles))+" tweets from "+x)
    for i in listOfFiles :
        if i.endswith('.json') :
            json_count += 1
            preprocessData(i)
    print("Totally processed "+str(json_count)+"JSONS")

if __name__ == '__main__':
    start()
    #preprocessData('HillaryClinton_mention_601.json')
