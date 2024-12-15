import pygame

class MeleeAttack:
    def __init__(self, attacker, x, y, width, height, damage):
        self.attacker = attacker
        self.hitbox = pygame.Rect(x, y, width, height)
        self.damage = damage

    def check_collision(self, target_rect):
        """Checks if the attack hitbox collides with the target rectangle."""
        return self.hitbox.colliderect(target_rect)


class Projectile:
    def __init__(self, attacker, x, y, velocity_x, velocity_y, width, height, damage):
        self.attacker = attacker
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.hitbox = pygame.Rect(x, y, width, height)
        self.damage = damage

    def update(self):
        """Updates the projectile's position."""
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.hitbox.x = self.x
        self.hitbox.y = self.y

    def check_collision(self, target_rect):
        """Checks if the projectile hitbox collides with the target rectangle."""
        return self.hitbox.colliderect(target_rect)
