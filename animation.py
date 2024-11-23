import pygame

# definir une classe qui va s ocupper des animations
class AnimateSprite(pygame.sprite.Sprite):

    # definir les choses a faire a la creation de l'entite
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0 # commencer l'animation à l'image 0
        self.images = animations.get(sprite_name)

    # definir une methode pour animer le sprite
    def animate(self):
        # passer à l'image suivante
        self.current_image += 1

        # verifier si l'animation est arrivee à la fin, et la recommencer
        if self.current_image >= len(self.images):
            # remettre l'animation au debut
            self.current_image = 0

        # modifier l'image précédente par la suivante
        self.image = self.images[self.current_image]

# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # recuperer le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque image dans ce dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'images
    return images


# definir un dictioonaire qui va contenir les images chargees de chaque sprite
# mummy -> [...mummy1.png, ...mummy2.png, ...]
animations = {
    'mummy': load_animation_images('mummy')
}
