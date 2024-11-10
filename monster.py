import pygame
import random


#cree une classe qui va gere la notion de monstre dans notre jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        # infliger les degats
        self.health -= amount

        # verifier si son nouveau nombre de point de vie est inferieur ou egal a 0
        if self.health <= 0:
            # reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health


    def update_health_bar(self, surface):
        # definir une couleur pour notre jauge de vie (vert clair)
        bar_color = (111, 210, 46)
        # definir une couleur pour l'arriere plan de la jauge (gris fonce)
        back_bar_color = (60, 63, 60)

        # definir une couleur pour notre jauge de vie ainsi que sa largeur et son epaiseur
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        # definir la position de l'arriere plan de la jauge de vie
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # dessiner l'arriere plan de notre barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # dessiner notre barre de vie
        pygame.draw.rect(surface, bar_color, bar_position)


    def forward(self):
        #le deplacement ne se fait que si il y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
