from flask import Blueprint, render_template, request
import json, re
from .models import parse_adress, find_full_adress, get_wikipedia
from .settings import API_KEY

global user_place

views = Blueprint("views", __name__, static_folder="static", template_folder="templates")

@views.route('/')
def home():
    return render_template("base.html")

# Passer en POST
@views.route('/map/', methods=['GET'])
def map():
    data = request.args.to_dict()
    return render_template("maps.html", data=data, api_key=API_KEY)


@views.route('/api', methods=['POST'])
def api():
    user_request = request.form['user_data']
    user_request = parse_adress(user_request)
    full_adress = user_request #find_full_adress(user_request)
    user_request = re.sub('[%20]', ' ', user_request)
    wikipedia = get_wikipedia(user_request)
    r = {}
    r['adress'] = full_adress
    r['wiki'] = wikipedia
    return r
