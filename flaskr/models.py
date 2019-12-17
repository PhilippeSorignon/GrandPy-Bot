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
                phrase += word + "%20"

            word = ""
    phrase += re.sub('[ !?.]', '', word)

    if phrase[len(phrase) - 1] == ' ':
        phrase = phrase[:len(phrase) - 1]

    return phrase


def find_full_adress(user_adress):
    request_data = {'query':user_adress, 'key':API_KEY}

    r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?',\
     params=request_data).json()['results']

    return r[0]['formatted_address']
