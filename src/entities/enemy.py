import pygame
import random

class Enemy:
    def __init__(self, x, y, width, height, speed, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.health = health
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.patrol_direction = 1  # 1 for right, -1 for left
        self.patrol_distance = 50
        self.initial_x = x

    def move(self, tiles):
        """Moves the enemy, checking for collisions."""
        new_x = self.x + self.speed * self.patrol_direction
        new_hitbox = pygame.Rect(new_x, self.y, self.width, self.height)

        if not self.check_collision(new_hitbox, tiles):
            self.x = new_x
            self.hitbox.x = self.x
        else:
            self.patrol_direction *= -1
        
        if abs(self.x - self.initial_x) > self.patrol_distance:
            self.patrol_direction *= -1

    def check_collision(self, rect, tiles):
        """Checks if the enemy's rectangle collides with any tile."""
        for tile in tiles:
            if tile.type != "floor":
                continue
            tile_rect = pygame.Rect(tile.x * 16, tile.y * 16, 16, 16)
            if rect.colliderect(tile_rect):
                return True
        return False

    def take_damage(self, damage):
        """Reduces the enemy's health by the damage amount."""
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.__class__.__name__} took {damage} damage. Current health: {self.health}")

    def get_hitbox(self):
        """Returns the enemy's hitbox."""
        return self.hitbox
