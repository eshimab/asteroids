import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        print(f"init CircleShape()")
        # we will use this later 
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0) 
        self.radius = radius

    def draw(self, screen):
        # sub-classes must overide
        pass

    def update(self, dt): 
        # sub-classes must overide
        pass
