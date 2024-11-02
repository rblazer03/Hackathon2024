from os import walk
import pygame

def import_sprite(path):
    surface_list = []
    for _, __, img_file in walk(path):
        for image in img_file:
            full_path = f"{path}/{image}"
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)
    return surface_list

class Duck():
    def __init__(self):
        super().__init__()
        self._import_character_assets()

    def _import_character_assets(self):
        character_path = "/assets/ducky_sprite.png/"
        self.animations = {"idle": [], "walk": [],
            "jump": [], "fall": []}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_sprite(full_path)