from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Dicionário com informações dos filmes
filmes = {
    1: {
        'titulo': 'Anjos da Noite',
        'sinopse': 'Selene é uma vampira feroz que está em meio a uma guerra entre vampiros e lobisomens...',
        'elenco': 'Kate Beckinsale, Scott Speedman, Michael Sheen',
        'poster': 'img/cartaz/UnderworldBloodWars.jpg',  # Corrigido
    },
    2: {
        'titulo': 'Oppenheimer',
        'sinopse': 'O drama biográfico sobre J. Robert Oppenheimer...',
        'elenco': 'Cillian Murphy, Emily Blunt, Matt Damon, Robert Downey Jr.',
        'poster': 'img/cartaz/Oppenheimer.png',  # Corrigido
    },
    3: {
        'titulo': 'Viúva Negra',
        'sinopse': 'A espiã Natasha Romanoff confronta os eventos sombrios de seu passado...',
        'elenco': 'Scarlett Johansson, Florence Pugh, David Harbour, Rachel Weisz',
        'poster': 'img/cartaz/BlackWidow.jpg',  # Corrigido
    },
    4: {
        'titulo': 'Vingadores Endgame',
        'sinopse': 'Os Vingadores precisam lidar com a destruição causada por Thanos...',
        'elenco': 'Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth',
        'poster': 'img/cartaz/AvengersEndgame.jpg',  # Corrigido
    },
    5: {
        'titulo': 'Resident Evil 6: O Capitulo Final',
        'sinopse': 'Sobrevivente do massacre zumbi, Alice retorna para onde o pesadelo começou...',
        'elenco': 'Milla Jovovich, Ruby Rose, Iain Glen, Shawn Roberts',
        'poster': 'img/cartaz/ResidentEvil6.jpg',  # Corrigido
    },
}


def movie_detail(request, movie_id):
    filme = filmes.get(movie_id, {})
    return render(request, 'movie_detail.html', {'filme': filme})