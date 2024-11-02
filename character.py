import pygame
from support import import_sprite

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