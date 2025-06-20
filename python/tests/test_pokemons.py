import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '430ffe2ed3e8bc128b304ed792f8acd5'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '36315'

def test_status_code():
    respons = requests.get (url=f'{URL}trainers')
    assert respons.status_code == 200

def test_trainer_name():
    respons_trainer_name = requests.get (url=f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert respons_trainer_name.json()["data"][0]["trainer_name"] == 'Grinya'
