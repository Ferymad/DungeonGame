import pygame

class Spell:
    def __init__(self, x, y, width, height, damage):
        self.speed = 5
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.damage = damage
        self.active = True
        self.speed_x = 0
        self.speed_y = 0


    def update(self):
        # Update spell logic here
        self.x += self.speed_x
        self.y += self.speed_y

    def check_collision(self, hitbox):
        spell_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return spell_rect.colliderect(hitbox)

class Fireball(Spell):
    def __init__(self, x, y, width, height, damage):
        super().__init__(x, y, width, height, damage)
    
    def update(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        self.speed_x = dx / (dx**2 + dy**2)**0.5 * self.speed
        self.speed_y = dy / (dx**2 + dy**2)**0.5 * self.speed
