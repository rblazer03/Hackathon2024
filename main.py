import pygame
from player import Player
from plat_form import Platform

# Initialize pygame
pygame.init() 

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Duck Jump")

GRAVITY = 1
PLAYER_SPEED = 2

# Create sprite groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# Create the player sprite and pass the platforms group
player = Player(100, 300, GRAVITY, PLAYER_SPEED, platforms)

# Add player to sprite group
all_sprites.add(player)

# Create platforms
p1 = Platform(300, 550, 200, 60)
p2 = Platform(80, 400, 100, 30)
p3 = Platform(500, 300, 150, 30)

# Add platforms to sprite groups
all_sprites.add(p1, p2, p3)
platforms.add(p1, p2, p3)

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites    
    all_sprites.update()
    
    # Fill the screen with a background color 
    screen.fill((147, 210, 220))
    all_sprites.draw(screen)

    # Update the display
    pygame.display.update()

pygame.quit()
