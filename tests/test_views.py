from flask import Flask, url_for

def test_app(client):
    '''Test if the main page loads correctly'''
    assert client.get(url_for('views.home')).status_code == 200
