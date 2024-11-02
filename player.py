import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, gravity, speed):
        super().__init__() 

        # Load the sprite sheet image
        self.sprite_sheet = pygame.image.load("ducky_2_spritesheet.png").convert()

        # Create a surface for the player image and set its rect attribute
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.gravity = gravity
        self.speed = speed

    def get_image(self, x, y):
        """Extracts image from sprite sheet"""
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        image.set_colorkey((0, 0, 0))  # Transparent black background
        return image

    def update(self):
        """Update the player"""
        # Apply gravity
        self.vel_y += self.gravity

        # Move left/right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel_x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.vel_x = self.speed
        else:
            self.vel_x = 0

        # Jump if on the ground
        if keys[pygame.K_UP] and self.on_ground:
            self.vel_y = -20

        # Update position
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Check if on the ground
        if self.rect.bottom >= 600:  # Assuming ground level is at y=600
            self.rect.bottom = 600
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False
            
        # Check if fallen off bottom of screen
        if self.rect.top > 600:
            self.kill()
    