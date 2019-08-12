import unittest
import urllib.request as urllib2
import json
from summoner.info import Info

class Summoner():    
    def __init__(self, apikey):
        self._api_key = "api_key=" + apikey
        self._apiurl_byname = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"

    def get_summoner(self, summoner_name):
        url =  self._create_url(summoner_name)
        # セッション強制Close用
        try:
            session = urllib2.urlopen(url)
            summoner = json.loads(session.read().decode('utf-8'))
            return Info(summoner[summoner_name.lower()])
        
        except Exception as e:
            raise Exception(e)       

        finally:
            session.close()

    def _create_url(self, summoner_name):
        url = self._apiurl_byname
        url += summoner_name
        url += "?"
        url += self._api_key
        return url

