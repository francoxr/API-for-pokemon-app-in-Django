# Django
from typing import OrderedDict
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon

# Django Rest
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PokemonSerializer

# Create your views here.

"""V1"""

def index(request):
    return HttpResponse("hello pokemaniatics!")

class PokemonList(generics.ListAPIView):
    # API endpoint that allows Pokemon to be viewed.
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonOneList(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

"""V2"""

@api_view(['GET'])
def PokemonGetAll(request):
    """ API endpoint that allows Pokemon to be viewed."""
    pokemons = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemons, many=True)

    for pokemon in serializer.data:
        new_type_ids = sorted(pokemon['type_ids'], key = lambda i: i['id'], reverse=True)
        pokemon['type_ids'] = new_type_ids

    return Response(serializer.data)

@api_view(['GET'])
def PokemonGetOne(request, pk):
    """ API endpoint that returns a single customer by pk."""
    pokemon = Pokemon.objects.get(id=pk)
    serializer = PokemonSerializer(pokemon, many=False)

    new_type_ids = sorted(serializer.data['type_ids'], key = lambda i: i['id'], reverse=True)
    serializer._data['type_ids'] = new_type_ids

    return Response(serializer.data)

@api_view(['GET'])
def PokemonGetWithFilter(request):
    """API endpoint that returns a one or many pokemons depends a filter of request."""    

    # search , name of pokemon
    # min_price , range of price
    # max_price , range of price
    # types = fire,water,.. , type of 
    # offset=100 , range of id 
    # limit=100  , range of id 

    name = request.GET['search']
    type_ids = request.GET['type_ids']
    type_ids_split = type_ids.split(',')

    # min_price = request.GET['min_price'] or ''
    # max_price = request.GET['max_price'] or  ''

    print(type(type_ids_split), type_ids_split)
    
    # Primer filtro de prices
    # SELECT * FROM pokemon WHERE price BETWEEN min_price AND max_price; price(string)
    # pokemons = Pokemon.objects.filter(price__range=(min_price, max_price))


    # Segundo filtro de types, se consigue toda la tabla
    # SELECT * FROM pokemon_pokemon
	# JOIN pokemon_pokemon_type_ids ON pokemon_pokemon.id = pokemon_pokemon_type_ids.pokemon_id
	# JOIN pokemon_types ON pokemon_types.id = pokemon_pokemon_type_ids.types_id
    pokemons = Pokemon.objects.filter(type_ids__name__in=type_ids_split)

    # Tercer filtro de pokemon por nombre
    # SELECT * FROM Pokemon_pokemon WHERE name = name
    # pokemons = Pokemon.objects.filter(name=name)

    serializer = PokemonSerializer(pokemons, many=True)


    return Response(serializer.data)
    # return Response(type_ids_split)
