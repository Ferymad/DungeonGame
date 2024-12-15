import pygame

class Character:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, dx, dy):
        """Moves the character by dx and dy."""
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.hitbox.x = self.x
        self.hitbox.y = self.y

    def get_hitbox(self):
        """Returns the character's hitbox."""
        return self.hitbox
