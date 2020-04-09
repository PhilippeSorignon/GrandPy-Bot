from flaskr.models import Api

class TestView:
    test = Api()
    def test_parse_view(self):
        '''Test if the parse_view function return what we want'''
        self.test.parse_adress("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
        assert self.test.user_request == "OpenClassrooms"

        self.test.parse_adress("Bonjour, je cherche où se trouve la Tour Eiffel.")
        assert self.test.user_request == "Tour Eiffel"


'''def test_return_full_adress():
    \'''Test if the call to the google place API return what we expect\'''
    assert find_full_adress("OpenClassrooms") == "7 Cité Paradis, 75010 Paris, France"'''
