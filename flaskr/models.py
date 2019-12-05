import json
import re


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

    if phrase[len(phrase) - 1] == ' ':
        phrase = phrase[:len(phrase) - 1]

    return phrase
