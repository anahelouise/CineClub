from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Dicionário com informações dos filmes
filmes = {
    1: {
        'titulo': 'Resident Evil 6: O Capitulo Final',
        'sinopse': 'Sobrevivente do massacre zumbi, Alice retorna para onde o pesadelo começou...',
        'elenco': 'Milla Jovovich, Ruby Rose, Iain Glen, Shawn Roberts',
        'poster': 'img/cartaz/1-ResidentEvil6.jpg',  
    },
    2: {
        'titulo': 'Oppenheimer',
        'sinopse': 'O drama biográfico sobre J. Robert Oppenheimer...',
        'elenco': 'Cillian Murphy, Emily Blunt, Matt Damon, Robert Downey Jr.',
        'poster': 'img/cartaz/2-Oppenheimer.png',  
    },
    3: {
        'titulo': 'Anjos da Noite',
        'sinopse': 'Selene é uma vampira feroz que está em meio a uma guerra entre vampiros e lobisomens...',
        'elenco': 'Kate Beckinsale, Scott Speedman, Michael Sheen',
        'poster': 'img/cartaz/3-UnderworldBloodWars.jpg',  
    },
    4: {
        'titulo': 'Viúva Negra',
        'sinopse': 'A espiã Natasha Romanoff confronta os eventos sombrios de seu passado...',
        'elenco': 'Scarlett Johansson, Florence Pugh, David Harbour, Rachel Weisz',
        'poster': 'img/cartaz/4-BlackWidow.jpg', 
    },

    5: {
        'titulo': 'Deadpool & Wolverine',
        'sinopse': 'Deadpool e Wolverine se unem em uma nova aventura cheia de ação e humor, enfrentando inimigos poderosos e desafios inesperados.',
        'elenco': 'Ryan Reynolds, Hugh Jackman',
        'poster': 'img/cartaz/5-Deadpool&Wolverine.jpg',  
    },
    6: {
        'titulo': 'Vingadores: Endgame',
        'sinopse': 'Após os eventos devastadores de "Vingadores: Guerra Infinita", os Vingadores restantes tentam reverter as ações de Thanos e restaurar a ordem no universo.',
        'elenco': 'Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth, Scarlett Johansson, Jeremy Renner',
        'poster': 'img/cartaz/6-AvengersEndgame.jpg',
    },
    7: {
        'titulo': 'É Assim Que Acaba',
        'sinopse': 'Baseado no best-seller de Colleen Hoover, o filme conta a história de Lily Bloom, que enfrenta um relacionamento complicado com Ryle Kincaid, enquanto revisita seu passado e as lições de vida que aprendeu.',
        'elenco': 'Blake Lively, Justin Baldoni, Brandon Sklenar',
        'poster': 'img/cartaz/7-ÉAssimQueAcaba.jpg',
    },
    8: {
        'titulo': 'Velozes e Furiosos 6',
        'sinopse': 'Dom e sua equipe são recrutados por Hobbs para derrubar uma organização de mercenários habilidosos em direção ao caos global. Com a promessa de perdão total, eles precisam enfrentar inimigos letais e desafios perigosos.',
        'elenco': 'Vin Diesel, Paul Walker, Dwayne Johnson, Michelle Rodriguez, Jordana Brewster',
        'poster': 'img/cartaz/8-VelozesEFuriosos.png',
    },
    9: {
        'titulo': 'Lucy',
        'sinopse': 'Lucy, uma mulher comum, involuntariamente se transforma em uma super-humana ao ser exposta a uma droga experimental que aumenta sua capacidade cerebral, levando-a a desenvolver poderes extraordinários e uma sede de vingança.',
        'elenco': 'Scarlett Johansson, Morgan Freeman, Choi Min-sik',
        'poster': 'img/cartaz/9-Lucy.jpg',
    },
    10: {
        'titulo': 'A Falha de San Andreas',
        'sinopse': 'Após um terremoto devastador atingir a Califórnia, um piloto de resgate e sua ex-esposa precisam atravessar o estado em uma jornada perigosa para salvar sua filha em meio a desastres naturais catastróficos.',
        'elenco': 'Dwayne Johnson, Carla Gugino, Alexandra Daddario, Paul Giamatti',
        'poster': 'img/cartaz/10-AFalhaDeSanAndreas.jpg',
    },
}


def movie_detail(request, movie_id):
    filme = filmes.get(movie_id, {})
    return render(request, 'movie_detail.html', {'filme': filme})