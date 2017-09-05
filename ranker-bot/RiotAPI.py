import RiotConsts as Consts
import requests
class RiotAPI(object):

    def __init__(self, api_key):
        self.api_key = api_key

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                url=api_url
            ),
        params=args
            )
        print(response.url)
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['summoner'],
            names=name
        )
        return self._request(api_url)
