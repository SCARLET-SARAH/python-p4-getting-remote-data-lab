import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url
        self.response = None

    def get_response_body(self):
        try:
            self.response = requests.get(self.url)
            self.response.raise_for_status()
            return self.response.text
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def load_json(self):
        try:
            if self.response is None:
                self.get_response_body()
            return self.response.json()
        except json.JSONDecodeError as e:
            print(f"Error: {e}")
            return None