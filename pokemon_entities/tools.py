import json
import datetime

from .models import Pokemon, PokemonEntity

def load_pokemons():
    with open("pokemon_entities/pokemons.json") as database:
        pokemons = json.load(database)['pokemons']

    #creating pokemons and their entities
    for pokemon in pokemons:
        pkmn = Pokemon(
            title_ru=pokemon['title_ru'],
            title_en=pokemon['title_en'],
            title_jp=pokemon['title_jp'],
            description=pokemon['description']
            )
        pkmn.save()
        for pokemon_entity in pokemon['entities']:
            pkmn_entity = PokemonEntity(
                pokemon=pkmn,
                latitude=pokemon_entity['lat'],
                longitude=pokemon_entity['lon'],
                appeared_at = datetime.datetime.now(),
                dissapeared_at = datetime.datetime.now() + datetime.timedelta(days=1),
                level=pokemon_entity['level']
                )
            pkmn_entity.save()

    #adding evolutions
    for pokemon in pokemons:
        try:
            next_evolution_pkmn = Pokemon.objects.get(title_ru=pokemon['next_evolution']['title_ru'])
        except:
            continue
        pkmn = Pokemon.objects.get(title_ru=pokemon['title_ru'])
        pkmn.next_evolution = next_evolution_pkmn
        pkmn.save()