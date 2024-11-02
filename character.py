import pygame as pg
from glob import glob

screen = pg.display.set_mode((400, 400))

class Ducky(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animation = [pg.image.load(f) for f in glob("assets/idle_bounce/image1x1.png")]
        self.image = self.animation[0]
        self.rect = self.image.get_rect()

g = pg.sprite.Group()
sprite = Ducky()
g.add(sprite)
print(sprite)

loop = 1
while loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = 0
        if event.type == pg.KEYDOWN:
            print("go")
        g.draw(screen)
        pg.display.flip()
pg.quit()

# def import_sprite(path):
#     surface_list = []
#     for _, __, img_file in walk(path):
#         for image in img_file:
#             full_path = f"{path}/{image}"
#             img_surface = pygame.image.load(full_path).convert_alpha()
#             surface_list.append(img_surface)
#     return surface_list

# class Duck():
#     def __init__(self):
#         super().__init__()
#         self._import_character_assets()

#     def _import_character_assets(self):
#         character_path = "/assets/ducky_sprite.png/"
#         self.animations = {"idle": [], "walk": [],
#             "jump": [], "fall": []}
#         for animation in self.animations.keys():
#             full_path = character_path + animation
#             self.animations[animation] = import_sprite(full_path)