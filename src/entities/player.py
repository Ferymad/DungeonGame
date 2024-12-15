import pygame
from combat.attack import MeleeAttack
from combat.spell import Fireball
from core.settings import PLAYER_HEALTH, PLAYER_SPEED

class Warrior:
    def __init__(self, x, y, width, height, speed):
        self.attack_cooldown = 500
        self.spell_cooldown = 1000
        self.last_attack_time = 0
        self.last_spell_time = 0
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.health = PLAYER_HEALTH
        self.attacks = []
        self.spells = []

    def handle_input(self, event, tiles):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                attack = MeleeAttack(self.x, self.y, 16, 16, 10)
                self.attacks.append(attack)
            elif event.key == pygame.K_LCTRL:
                self.cast_spell(pygame.mouse.get_pos())

    def attack(self):
        if pygame.time.get_ticks() - self.last_attack_time < self.attack_cooldown:
            return None
        if self.attacks:
            self.last_attack_time = pygame.time.get_ticks()
            return self.attacks.pop(0)
        return None

    def cast_spell(self, target_position):
        if self.spells:
            return self.spells.pop(0)
    def cast_spell(self, target_position):
        if self.spells:
            return self.spells.pop(0)
        return None

    def take_damage(self, damage):
        self.health -= damage

    @property
    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, dx, dy, tiles):
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed

        if not self.collides_with_tiles(new_x, self.y, tiles):
            self.x = new_x
        if not self.collides_with_tiles(self.x, new_y, tiles):
            self.y = new_y

    def collides_with_tiles(self, x, y, tiles):
        player_rect = pygame.Rect(x, y, self.width, self.height)
        for tile in tiles:
            if tile.type != "floor" and player_rect.colliderect(tile.rect):
                return True
        return False

    def update(self):
        for attack in self.attacks:
            attack.update()
        for spell in self.spells:
            pass
