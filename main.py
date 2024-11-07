import pygame
pygame.init()

# generer la fenetre de notre jeux
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((500, 300))

running = True

# boucle tant que cette condition est vrai
while running:

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
