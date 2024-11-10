import pygame


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
        self.rect.x = 1000
        self.rect.y = 540
        self.velocity = 2

    def update_health_bar(self):
        # definir une couleur pour notre jauge de vie (vert clair)
        bar_color = (111, 210, 46)

        # definir une couleur pour notre jauge de vie ainsi que sa largeur et son epaiseur
        bar_position = [self.rect.x, self.rect.y, self.health, 5]

    def forward(self):
        #le deplacement ne se fait que si il y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
