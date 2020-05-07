import flaskr.models as models

from io import BytesIO
import json

class TestView:
    """Tests"""
    test = models.Api()
    def test_parse_view(self):
        '''Test if the parse_view function return what we want'''
        self.test.parse_adress("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
        assert self.test.user_request == "OpenClassrooms"

        self.test.parse_adress("Bonjour, je cherche où se trouve la Tour Eiffel.")
        assert self.test.user_request == "Tour Eiffel"

    def test_nominatim(self, monkeypatch):
        """Mock to test if the adress is correct"""
        self.test.parse_adress("Bonjour, je cherche où se trouve la Tour Eiffel.")

        r = [{
            'place_id': 80582518,
            'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
            'osm_type': 'way',
            'osm_id': 5013364,
            'boundingbox': ['48.8574753', '48.8590465', '2.2933084', '2.2956897'],
            'lat': '48.858260200000004',
            'lon': '2.2944990543196795',
            'display_name':
            'Tour Eiffel, 5, Avenue Anatole France, Quartier du Gros-Caillou, Paris, Île-de-France, France métropolitaine, 75007, France',
            'class': 'tourism',
            'type': 'attraction',
            'importance': 0.7868325701744197,
            'icon':
            'https://nominatim.openstreetmap.org/images/mapicons/poi_point_of_interest.p.20.png'
            }]

        def mockreturn(request, params):
            """Mock Definition"""
            class faker:
                """Fake Return"""
                @staticmethod
                def json():
                    return r

            return faker

        monkeypatch.setattr(models.requests, 'get', mockreturn)

        self.test.find_full_adress()

        assert self.test.full_adress == "Tour Eiffel, 5, Avenue Anatole France, Quartier du Gros-Caillou, Paris, Île-de-France, France métropolitaine, 75007, France"


    def test_wikipedia(self, monkeypatch):

        r = {'batchcomplete': '', 'query': {'pages': {'1359783': {'pageid': 1359783, 'ns': 0, 'title': 'Tour Eiffel', 'extract': "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France. Construite par Gustave Eiffel et ses collaborateurs pour l’Exposition universelle de Paris de 1889, et initialement nommée « tour de 300 mètres », ce monument est devenu le symbole de la capitale française, et un site touristique de premier plan : il s’agit du troisième site culturel français payant le plus visité en 2015, avec 6,9 millions de visiteurs, en 2011 la cathédrale Notre-Dame de Paris était en tête des monuments à l'accès libre avec 13,6 millions de visiteurs estimés mais il reste le monument payant le plus visité au monde,. Depuis son ouverture au public, elle a accueilli plus de 300 millions de visiteurs.\nD’une hauteur de 312 mètres à l’origine, la tour Eiffel est restée le monument le plus élevé du monde pendant quarante ans. Le second niveau du troisième étage, appelé parfois quatrième étage, situé à 279,11 mètres, est la plus haute plateforme d'observation accessible au public de l'Union européenne et la deuxième plus haute d'Europe, derrière la tour Ostankino à Moscou culminant à 337 mètres. La hauteur de la tour a été plusieurs fois augmentée par l’installation de nombreuses antennes. Utilisée dans le passé pour de nombreuses expériences scientifiques, elle sert aujourd’hui d’émetteur de programmes radiophoniques et télévisés.\n\n"}}}}


        def mockreturn(request, params):
            """Mock Definition"""
            class faker:
                """Fake Return"""

                @staticmethod
                def json():
                    return r

            return faker

        monkeypatch.setattr(models.requests, 'get', mockreturn)

        self.test.get_wikipedia()

        assert self.test.wikipedia_description == r['query']['pages']['1359783']['extract']
