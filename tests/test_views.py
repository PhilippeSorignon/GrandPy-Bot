from flask import Flask, url_for

def test_app(client):
    assert client.get(url_for('home')).status_code == 200
