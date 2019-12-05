from flaskr.models import parse_adress

def test_parse_view():
    '''Test if the parse_view function return what we want'''
    assert parse_adress("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?") == "OpenClassrooms"

    assert parse_adress("Bonjour, je cherche où se trouve la Tour Eiffel.") == "Tour Eiffel"
