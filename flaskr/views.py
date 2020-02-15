from flask import Blueprint, render_template, request
import json, re
from .models import Api
from .settings import API_KEY

global user_place

views = Blueprint("views", __name__, static_folder="static", template_folder="templates")

api_instance = Api()

@views.route('/')
def home():
    return render_template("base.html")

# Passer en POST
@views.route('/map')
def map():
    data = {}
    data['adress'] = api_instance.full_adress
    data['wiki'] = api_instance.wikipedia_description
    return render_template("maps.html", data=data, api_key=API_KEY)


@views.route('/api', methods=['POST'])
def api():
    api_instance.parse_adress(request.form['user_data'])
    #full_adress = user_request #find_full_adress(user_request)
    api_instance.full_adress = api_instance.user_request
    #user_request = re.sub('[%20]', ' ', user_request)
    api_instance.get_wikipedia()
    return 'ok'
