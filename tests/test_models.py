from flaskr.models import parse_adress, find_full_adress

def test_parse_view():
    '''Test if the parse_view function return what we want'''
    assert parse_adress("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?") == "OpenClassrooms%20"

    assert parse_adress("Bonjour, je cherche où se trouve la Tour Eiffel.") == "Tour%20Eiffel"


'''def test_return_full_adress():
    \'''Test if the call to the google place API return what we expect\'''
    assert find_full_adress("OpenClassrooms") == "7 Cité Paradis, 75010 Paris, France"'''
