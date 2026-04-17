import requests
import random

async def buscar_detalhes_movimento(url_movimento):
    try:
        resposta = requests.get(url_movimento)
        if resposta.status_code == 200:
            data = resposta.json()
            return {
                'name': data['name'],
                'category': data['damage_class']['name'],
                'power': data['power'] if data['power'] else 0
            }
    except:
        return None

async def pokemon_aleatorio():
    id_poke = random.randint(1, 151)
    url = f'https://pokeapi.co/api/v2/pokemon/{id_poke}/'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return {
            'nome': dados['name'].upper(),
            'moves_urls': [m['move']['url'] for m in dados['moves']]
        }
    raise Exception('Falha ao conectar com PokeAPI')