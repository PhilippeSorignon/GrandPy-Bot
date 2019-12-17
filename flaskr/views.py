from flask import Blueprint, render_template, request
import json
from .models import parse_adress, find_full_adress

global user_place

views = Blueprint("views", __name__, static_folder="static", template_folder="templates")

@views.route('/')
def home():
    return render_template("base.html")


@views.route('/map/<adress>')
def map(adress=None):
    return render_template("maps.html", adress=adress)


@views.route('/api', methods=['POST'])
def api():
    user_request = request.form['user_data']
    user_request = parse_adress(user_request)
    full_adress = user_request #find_full_adress(user_request)
    return full_adress
