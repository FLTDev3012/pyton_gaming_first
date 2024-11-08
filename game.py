import pygame
from player import Player

# creer une seconde classe qui va representer notre jeu

class Game:

    def __init__(self):
        # generer notre joueur
        self.player = Player()
        self.pressed = {}
