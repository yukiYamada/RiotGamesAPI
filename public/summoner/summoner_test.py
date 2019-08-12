import unittest
import summoner

class Test_MyFirstApi(unittest.TestCase):
    def setUp(self):
        print("setup-start")
        self.apikey = "apikey"
        self.actualObj = summoner.summoner.Summoner(self.apikey)
        print("setup-end")

    def test_create_url(self):
        print("test_create_url-start")
        summoner_name = "testname"
        expected = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?" + "api_key=" + self.apikey
        actual = self.actualObj._create_url(summoner_name)

        self.assertEqual(expected, actual)
        print("test_create_url-end")
        
if __name__ == "__main__":
    unittest.main()