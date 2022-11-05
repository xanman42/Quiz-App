import requests

parameters = {
    'amount': 20,
    'category': 18,
    'type': 'boolean'
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()['results']