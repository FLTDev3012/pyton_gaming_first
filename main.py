import pygame
from game import Game
pygame.init()

# generer la fenetre de notre jeux
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# importer et charger l'arriere plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# charger notre jeu
game = Game()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    # appliquer l'image de notre joueur
    screen.blit(game.player.image, game.player.rect)

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
