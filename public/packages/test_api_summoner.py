import unittest
from mock import MagicMock, patch
from api.summoner.summoner_reader import Reader
from api.summoner.info import Info
import urllib.request as urllib2

class Test_Api_Summoner(unittest.TestCase):
    def setUp(self):
        print("setup-start")
        self.apikey = "apikey"
        self.reader = Reader(self.apikey)
        self.test_summoner_name = "testname"
        print("setup-end")

    def test_create_url(self):
        print("test_create_url-start")
        expected = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + self.test_summoner_name + "?" + "api_key=" + self.apikey
        actual = self.reader._create_url(self.test_summoner_name)

        self.assertEqual(expected, actual)
        print("test_create_url-end")       

if __name__ == "__main__":
    unittest.main()