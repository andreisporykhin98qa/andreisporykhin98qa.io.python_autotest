import requests
import pytest

#тест на проверку статус кода 201 при создание покемона
def test_status_code_create_pokemon():
    token = '59279395edd1be3863c92c8f8bcce186' 
    response = requests.post('https://api.pokemonbattle.ru/v2/pokemons', headers={'trainer_token': token}, json={
    "name": "generate",
    "photo_id": -1
})
    assert response.status_code == 201

#тест на проверку статус кода 200 при отправке запроса, и при получение нужных данных
def test_trainer_name():
    response = requests.get('https://api.pokemonbattle.ru/v2/trainers', params={'trainer_id': 21169})
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body['data'][0]['trainer_name'] == 'Андрей443'