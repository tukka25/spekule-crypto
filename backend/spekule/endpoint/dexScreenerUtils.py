import requests, json

def get_token_addresses():
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)
    data = response.json()
    token_addresses = [token['id'] for token in data]
    return token_addresses