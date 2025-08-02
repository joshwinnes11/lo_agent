import requests

class PropertyInfoRetriever():
    def __init__(self, address):
        self.address = address
        
    def get_list_price(self):
        url = "https://zillow-com1.p.rapidapi.com/zestimate"
        payload = {"address": self.address}
        headers = {
            "x-rapidapi-key": "268487c947mshee2b17b8a5f2e29p1b21ddjsnc38181cb880b",
            "x-rapidapi-host": "zillow-com1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=payload).json()
        return response