import requests

class APIClient:
    
    def __init__(self, base_url):
        self.base_url = base_url
        
    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur API : {e}")
            return None
        
    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur API : {e}")
            return None
        
    def put(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.put(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur API : {e}")
            return None
    
    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.delete(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur API : {e}")
            return None