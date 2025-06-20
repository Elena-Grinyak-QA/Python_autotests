import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '430ffe2ed3e8bc128b304ed792f8acd5'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_createpokemons = {
    "name": "Васяш",
    "photo_id": -1
}

respons_create = requests.post (url=f'{URL}pokemons', headers=HEADER, json=body_createpokemons)
print(respons_create.text)

pokemon_id = respons_create.json()['id']
print(pokemon_id)

body_change = {
    "pokemon_id": pokemon_id,
    "name": "Кукумбер",
    "photo_id": -1
}

body_pokeball = {
    "pokemon_id": pokemon_id
}

respons_change = requests.put (url=f'{URL}pokemons', headers=HEADER, json=body_change)
print(respons_change.text)

respons_pokeball = requests.post (url=f'{URL}trainers/add_pokeball', headers=HEADER, json=body_pokeball)
print(respons_pokeball.text)