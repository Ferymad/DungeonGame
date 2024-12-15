import pygame

class MeleeAttack:
    def __init__(self, attacker, x, y, width, height, damage):
        self.attacker = attacker
        self.hitbox = pygame.Rect(x, y, width, height)
        self.damage = damage

    def check_collision(self, target_rect):
        """Checks if the attack hitbox collides with the target rectangle."""
        return self.hitbox.colliderect(target_rect)
