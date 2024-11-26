import pygame
import random
import animation


#cree une classe qui va gere la notion de monstre dans notre jeu
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.velocity = random.randint(1, 3)
        self.start_animation()

    def damage(self, amount):
        # infliger les degats
        self.health -= amount

        # verifier si son nouveau nombre de point de vie est inferieur ou egal a 0
        if self.health <= 0:
            # reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

            # si la barre d'evenement est a son maximum
            if self.game.comet_event.is_full_loaded():
                # retirer du jeu
                self.game.all_monsters.remove(self)

                # apeller la methode pour essayer de declencher la pluie de cometes
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)


    def update_health_bar(self, surface):

        # dessiner l'arriere plan de notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


    def forward(self):
        #le deplacement ne se fait que si il y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # infliger des degats (au joueur)
            self.game.player.damage(self.attack)

# definir une classe pour la momie
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, 'mummy', (130, 130))

# definir une classe pour l'alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, 'alien', (300, 300), 130)
