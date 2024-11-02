import pygame
from player import Player

# Initialize pygame
pygame.init() 

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Duck Jump")

GRAVITY = 1
PLAYER_SPEED = 5

#player sprite
player = Player(100, 300, GRAVITY, PLAYER_SPEED)
all_sprites = pygame.sprite.Group(player)

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
