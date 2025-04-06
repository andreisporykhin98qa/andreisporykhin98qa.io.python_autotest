import requests

token = '59279395edd1be3863c92c8f8bcce186' 
url = 'https://api.pokemonbattle.ru'  
responce_add_pokemon = requests.post (f'{url}/v2/pokemons', headers={'trainer_token' : token}, json={
    "name": "generate",
    "photo_id": -1
})

response_body = responce_add_pokemon.json()
pokemon_id = response_body['id']

print(responce_add_pokemon.text)


change = requests.put (f'{url}/v2/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": -1
})
print(change.text)

add_pokeboll = requests.post (f'{url}/v2/trainers/add_pokeball', headers={'trainer_token' : token}, json={
    "pokemon_id": pokemon_id
})
print(add_pokeboll.text)