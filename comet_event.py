import pygame

# creer une classe pour gerer cet evenement
class CometFallEvent:

    # lors du chargement -> creer un compteur
    def __init__(self):
        self.percent = 0

    def add_percent(self):
        self.percent += 1

    def update_bar(self, surface):
        #barre noir (en arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # l'axe des x
            surface.get_height(), # l'axe des y
            surface.get_width(), # longueur de la fenetre
            10 # epaisseur de la barre
        ])
        #barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0, # l'axe des x
            surface.get_height(), # l'axe des y
            (surface.get_width() / 100) * self.percent , # longueur de la fenetre
            10 # epaisseur de la barre
        ])
