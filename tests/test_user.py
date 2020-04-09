from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import time

from flaskr import create_app

class TestUser(LiveServerTestCase):
    def create_app(self):
        app = create_app()

        return app

    # Méthode exécutée avant chaque test
    def setUp(self):
        """Setup the test driver and create test users"""
        # Le navigateur est Firefox
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 1000)

    # Méthode exécutée après chaque test
    def tearDown(self):
        self.driver.quit()

    def test_user(self):
        self.driver.get(self.get_server_url())

        self.wait.until(lambda driver: self.driver.find_element_by_id("form_area").is_displayed())

        self.driver.find_element_by_id("form_area").send_keys("Connais-tu l'adresse du Mucem ?")

        ActionChains(self.driver).key_down(Keys.RETURN).key_up(Keys.RETURN).perform()

        self.wait.until(lambda driver: self.driver.find_element_by_id("text_result").is_displayed())

        result = self.driver.find_element_by_id("text_result").text
        result_wiki = self.driver.find_element_by_id("text_wiki").text

        assert "Bien sûr mon poussin ! La voici : Musée des Civilisations de l'Europe et de la Méditerranée, 1, Promenade Robert Laffont, La Joliette, Deuxième secteur, Marseille, Provence-Alpes-Côte d'Azur, France métropolitaine, 13002, France" in result
        assert "Le musée des Civilisations de l'Europe et de la Méditerranée (Mucem) est un musée national situé à Marseille. Il a ouvert le 7 juin 2013, lorsque Marseille était la Capitale européenne de la culture" in result_wiki
