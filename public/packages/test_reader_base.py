from api.reader_base import Reader_Base
from api.other_parameters import Other_Parameters, None_OtherParameters
import unittest

class Test_Reader_Base(unittest.TestCase):
    def setUp(self):
        print("setup-start")
        self.apikey = "apikey"
        self.actualObj = Reader_Base(self.apikey)       

    def test_create_url(self):
        """
        Reader_Base.class _create_url method test.      
        """
        
        print("no other parameter.")
        main_parameter = "summoner_test"
        "None_OhterPrameters() is Reader_Base constracter Optional Aruguments default"
        actual = self.actualObj._create_url(main_parameter, None_OtherParameters())

        expected = main_parameter + "?" + "api_key=" + self.apikey
        self.assertEqual(actual, expected) 

        print("consider other parameter")        
        other_parameter = Other_Parameters({"summonerID":"test_summoner","account":"test_account_id"})
        actual = self.actualObj._create_url(main_parameter, other_parameter)
        expected = main_parameter + "?summonerID=" + "test_summoner" + "?account=" + "test_account_id" + "?" + "api_key=" + self.apikey
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()