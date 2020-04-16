from flaskr.models import Api

import urllib.request

from io import BytesIO
import json

class TestView:
    test = Api()
    def test_parse_view(self):
        '''Test if the parse_view function return what we want'''
        self.test.parse_adress("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
        assert self.test.user_request == "OpenClassrooms"

        self.test.parse_adress("Bonjour, je cherche où se trouve la Tour Eiffel.")
        assert self.test.user_request == "Tour Eiffel"

    def test_http_return(self, monkeypatch):
        self.test.parse_adress("Bonjour, je cherche où se trouve la Tour Eiffel.")

        r = [{'place_id': 80582518, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright', 'osm_type': 'way', 'osm_id': 5013364, 'boundingbox': ['48.8574753', '48.8590465', '2.2933084', '2.2956897'], 'lat': '48.858260200000004', 'lon': '2.2944990543196795', 'display_name': 'Tour Eiffel, 5, Avenue Anatole France, Quartier du Gros-Caillou, Paris, Île-de-France, France métropolitaine, 75007, France', 'class': 'tourism', 'type': 'attraction', 'importance': 0.7868325701744197, 'icon': 'https://nominatim.openstreetmap.org/images/mapicons/poi_point_of_interest.p.20.png'}]

        def mockreturn(request):
            return BytesIO(json.dumps(r).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        self.test.find_full_adress()

        assert self.test.full_adress == "Tour Eiffel, 5, Avenue Anatole France, Quartier du Gros-Caillou, Paris, Île-de-France, France métropolitaine, 75007, France"
