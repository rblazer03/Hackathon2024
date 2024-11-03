# Base code from: https://coderslegacy.com/python/pygame-platformer-game-development/
import pygame
from pygame.locals import *
import sys
import random
 
pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional
 
# determine the main platform size
HEIGHT = 800
WIDTH = 1000

# control duck movement speed
ACC = 0.5
FRIC = -0.12

# control screen update speed
FPS = 60
FramePerSec = pygame.time.Clock()

# create main display
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Duck Jump")

#sprite animations
ducky_sprite = [pygame.image.load("assets/walk_bounce/image1x1.png"),
                pygame.image.load("assets/walk_bounce/image2x1.png"),
                pygame.image.load("assets/walk_bounce/image3x1.png"),
                pygame.image.load("assets/walk_bounce/image4x1.png"),
                pygame.image.load("assets/walk_bounce/image5x1.png"),
                pygame.image.load("assets/walk_bounce/image6x1.png")]
walking = False

class Player(pygame.sprite.Sprite):
    # create/initialize sprite
    def __init__(self):
        super().__init__() 
        # creat sprite
        self.surf = (pygame.image.load("assets/ide_normal/image1x1.png"))
        self.rect = self.surf.get_rect()
        # set sprite position and initial speed
        self.pos = vec((10, 360))
        self.vel = vec(0,0)
        self.acc = vec((0,0),(0,0))
 
    def move(self):
        self.acc = vec(0,0.5)
        frame = 0
    
        pressed_keys = pygame.key.get_pressed()    
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
            walking = True
            P1.surf = ducky_sprite[frame]
            frame +=1
            if frame < 5:
                frame = 0
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        if pressed_keys[K_UP]:
            #jump limit
            hits = pygame.sprite.spritecollide(self, platforms, False)
            if hits:
                self.vel.y = -15

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        # keeps duck from going off screen
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
             
        self.rect.midbottom = self.pos
 
    # keeps ducky from going through platforms
    def update(self):
        hits = pygame.sprite.spritecollide(P1 ,platforms, False)
        if P1.vel.y > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1
 
 
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((0,128,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
 
    def move(self):
        pass

class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()
        # Create a platform surface with the given width and height
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0, 128, 0))  # Fill with green color for visibility
        self.rect = self.surf.get_rect(center=(x, y))  # Position the platform

 
PT1 = Ground()
PT2 = Platform(100, 30, 300, 600)
P1 = Player()
 
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(PT2)
all_sprites.add(P1)
 
platforms = pygame.sprite.Group()
platforms.add(PT1)
platforms.add(PT2)

characters = pygame.sprite.Group()
characters.add(P1)
 
 
while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.KEYDOWN:    
        #     if event.key == pygame.K_SPACE:
        #         P1.jump()

    # Fill the screen with a background color 
    gameDisplay.fill((147, 210, 220))
    P1.update()
 
    for entity in all_sprites:
        gameDisplay.blit(entity.surf, entity.rect)
        
    for entity in characters:
        entity.move()
 
    pygame.display.update()
    FramePerSec.tick(FPS)
