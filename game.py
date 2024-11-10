from player import Player
from monster import Monster
import pygame


# creer une seconde classe qui va representer notre jeu

class Game:

    def __init__(self):
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # definir un groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
