from crud.base import crudbase
import requests
import json
import csv


def create_csv(name: str, colums: list, df: tuple):
    with open("{}.csv".format(name), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(colums)  # escribir los encabezados de columna
        writer.writerows(df)  # escribir los datos de la consulta


# buscamos todos los pokemos.
data = requests.get('https://pokeapi.co/api/v2/pokemon')
data = json.loads(data.text)

# Recorremos cada pokemon para obtener su informacion.
for pk in data['results']:

    # Se hace
    inf_pk = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pk["name"]))
    inf_pk = json.loads(inf_pk.text)
    pokemon_id = crudbase.insert_data('pokemons', '(name, image_url)', (inf_pk["name"], inf_pk["sprites"]["front_default"]))

    # Insertar las habilidades en la tabla pokemon_abilities
    for ability in inf_pk["abilities"]:
        crudbase.insert_data('pokemon_abilities', '(pokemon_id, ability)',(pokemon_id,  ability["ability"]["name"]))

    # Insertar las estadísticas en la tabla pokemon_stats
    for stat in inf_pk["stats"]:
        crudbase.insert_data('pokemon_stats', '(pokemon_id, stat, base_stat)', (pokemon_id, stat["stat"]["name"], str(stat["base_stat"])), markers_num=3)

    # Insertar los tipos en la tabla pokemon_types
    for type_ in inf_pk["types"]:
        crudbase.insert_data('pokemon_types', '(pokemon_id, type)', (pokemon_id, type_["type"]["name"]))

#  Pokemones con más de dos tipos
df_1 = crudbase.select("pokemons", "WHERE (SELECT COUNT(*) FROM pokemon_types WHERE pokemon_types.pokemon_id = pokemons.id) > 2")

# Tipo que más se repite
df_2 = crudbase.select("pokemon_types", "GROUP BY type ORDER BY COUNT(*) DESC LIMIT 1",fields="type, COUNT(*)")
df = df_1 + df_2

create_csv("pokemones",["id","name","url"],df)

