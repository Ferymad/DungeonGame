import pygame

class Spell:
    def __init__(self, x, y, width, height, damage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.damage = damage
        self.active = True

    def update(self):
        # Update spell logic here
        pass

    def check_collision(self, hitbox):
        spell_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return spell_rect.colliderect(hitbox)

class Fireball(Spell):
    def __init__(self, x, y, width, height, damage):
        super().__init__(x, y, width, height, damage)
