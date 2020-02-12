import json
import requests
import re
from .settings import API_KEY


def parse_adress(user_input):
    with open('flaskr/static/fr.txt') as json_file:
        stop_words = json.load(json_file)
    phrase = ""
    word = ""
    for i in range(len(user_input)):
        if user_input[i] != " " and user_input[i] != "'":
            word += (user_input[i])
        else:
            if word in stop_words:
                phrase = ""
            else:
                phrase += word + " "

            word = ""
    phrase += re.sub('[ !?.]', '', word)
    phrase = re.sub(' ', '%20', phrase)

    if phrase[len(phrase) - 1] == ' ':
        phrase = phrase[:len(phrase) - 1]

    return phrase


def find_full_adress(user_adress):
    request_data = {'query':user_adress, 'key':API_KEY}

    r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?',\
     params=request_data).json()['results']

    return r[0]['formatted_address']


def get_wikipedia(user_input):
    # format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Paris
    request_data = {'format':'json', 'action':'query', 'prop':'extracts', 'exintro':'', 'explaintext':'', 'redirects':'1', 'titles':user_input}

    r = requests.get('https://fr.wikipedia.org/w/api.php?', params=request_data).json()['query']

    phrase = re.sub('[\[\]]', '', r['pages'][list(r['pages'].keys())[0]]['extract'])
    phrase = re.sub(' ', '%20', phrase)
    return phrase
