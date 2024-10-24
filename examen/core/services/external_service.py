import requests

def get_external_data():
    response = requests.get('https://api.example.com/data')
    return response.json()