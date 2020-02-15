import json
import requests
import re
from .settings import API_KEY

'''Make the APIs calls and return formatted data'''
class Api:
    '''Init constructor'''
    def __init__(self):
        self.user_request = ''
        self.full_adress = ''
        self.wikipedia_description = ''

    '''Return the place to search from the user input'''
    def parse_adress(self, user_input):
        with open('flaskr/static/fr.txt') as json_file:
            stop_words = json.load(json_file)
        word = ""
        for i in range(len(user_input)):
            if user_input[i] != " " and user_input[i] != "'":
                word += (user_input[i])
            else:
                if word in stop_words:
                    self.user_request = ""
                else:
                    self.user_request += word + " "

                word = ""
        self.user_request += re.sub('[ !?.]', '', word)

        if self.user_request[len(self.user_request) - 1] == ' ':
            self.user_request = self.user_request[:len(self.user_request) - 1]


    '''Return the exact adress using the Google Places API'''
    def find_full_adress(self, user_adress):
        request_data = {'query':user_adress, 'key':API_KEY}

        r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?',\
         params=request_data).json()['results']

        self.full_adress = r[0]['formatted_address']


    '''Return the Wikipedia introduction'''
    def get_wikipedia(self):
        # format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Paris
        request_data = {'format':'json', 'action':'query', 'prop':'extracts',
                        'exintro':'', 'explaintext':'', 'redirects':'1', 'titles':self.user_request}

        r = requests.get('https://fr.wikipedia.org/w/api.php?', params=request_data).json()['query']

        self.wikipedia_description = re.sub('[\[\]]', '',
                                            r['pages'][list(r['pages'].keys())[0]]['extract'])
