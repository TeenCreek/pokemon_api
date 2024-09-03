import pokebase as pb
from django.shortcuts import render


def pokemon_list(request):
    pokemons = pb.APIResourceList('pokemon')

    return render(request, 'pokedata/pokemon_list.html', {'pokemons': pokemons})


def pokemon_detail(request, name):
    poke = pb.pokemon(name)

    return render(request, 'pokedata/pokemon_detail.html', {'pokemon': poke})
