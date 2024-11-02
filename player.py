import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 

        # Load the sprite sheet image
        self.sprite_sheet = pygame.image.load("ducky_2_spritesheet.png").convert()

        # Create a surface for the player image and set its rect attribute
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_image(self, x, y):
        """Extracts image from sprite sheet"""
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        image.set_colorkey((0, 0, 0))  # Transparent black background
        return image

    def update(self):
        """Update the player"""
        pass