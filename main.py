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

# initialiser l'horloge
clock = pygame.time.Clock()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    # appliquer l'image de notre joueur
    screen.blit(game.player.image, game.player.rect)

    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # recuperer les monstres de notre jeu
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # appliquer l'ensemble des images de mon groupe de monstres
    game.all_monsters.draw(screen)

    # verifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # mettre a jour l'ecran
    pygame.display.flip()

    # limiter la vitesse de la boucle de jeu à 30 FPS
    clock.tick(50)  # Limite la cadence à 30 images par seconde


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
