from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Dicionário com informações dos filmes
filmes = {
    1: {
        'titulo': 'Anjos da Noite',
        'sinopse': 'Selene é uma vampira feroz que está em meio a uma guerra entre vampiros e lobisomens. Sua missão é proteger sua raça enquanto busca respostas sobre seu próprio passado.',
        'elenco': 'Kate Beckinsale, Scott Speedman, Michael Sheen',
        'poster': 'static/img/cartaz/UnderworldBloodWars.jpg'
    },
    2: {
        'titulo': 'Oppenheimer',
        'sinopse': 'O drama biográfico sobre J. Robert Oppenheimer, o cientista que liderou o Projeto Manhattan e ajudou a desenvolver a primeira bomba atômica durante a Segunda Guerra Mundial.',
        'elenco': 'Cillian Murphy, Emily Blunt, Matt Damon, Robert Downey Jr.',
        'poster': 'static\img\cartaz\Oppenheimer.png'
    },
    3: {
        'titulo': 'Viúva Negra',
        'sinopse': 'A espiã Natasha Romanoff, também conhecida como Viúva Negra, confronta os eventos sombrios de seu passado enquanto enfrenta uma nova ameaça global.',
        'elenco': 'Scarlett Johansson, Florence Pugh, David Harbour, Rachel Weisz',
        'poster': 'static\img\cartaz\BlackWidow.jpg'
    },
    4: {
        'titulo': 'Vingadores Endgame',
        'sinopse': 'Os Vingadores precisam lidar com a destruição causada por Thanos e buscar uma forma de restaurar o universo.',
        'elenco': 'Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth',
        'poster': 'static\img\cartaz\AvengersEndgame.jpg'
    },
}

def movie_detail(request, movie_id):
    filme = filmes.get(movie_id, {})
    return render(request, 'movie_detail.html', {'filme': filme})