import random
import requests

BASE_URL = "https://smogonapi.herokuapp.com"


def api_call(name_or_id):
    url = f"{BASE_URL}/{name_or_id}"
    response = requests.get(url)
    return response.json()


# print(api_call("GetPokemonByGenAndTier/bw/ou"))
print(api_call("getPokemonStatsHistorical/dratini"))
