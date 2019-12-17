from flask import Flask, url_for
import json

def test_app(client):
    '''Test if the main page loads correctly'''
    assert client.get(url_for('views.home')).status_code == 200

def test_post(client):
    data = {'user_data': "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"}
    response = client.post('/api', data=json.dumps(data))
    assert response == "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
