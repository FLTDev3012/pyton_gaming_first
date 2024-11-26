import pygame
import math
from game import Game
pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 60


# generer la fenetre de notre jeux
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# importer et charger l'arriere plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# importer et charger notre banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer et charger notre bouton pour lancer le jeu
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)


# charger notre jeu
game = Game()

# initialiser l'horloge
clock = pygame.time.Clock()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    # verifier si le jeu a commence ou non
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)
    # verifier si le jeu n'a pas commence
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # fixer le nombre de fps sur ma clock
    clock.tick(FPS)

    # mettre a jour l'ecran
    pygame.display.flip()


    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # detecter si la touche espace est enclenchee pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                game.start()
