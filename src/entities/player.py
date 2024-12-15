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


class Warrior(Character):
    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height, speed)
        self.attack_damage = 10
        self.defense = 5
        self.max_health = 100
        self.current_health = self.max_health

    def take_damage(self, damage):
        """Reduces the character's health by the damage amount."""
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
        print(f"Warrior took {damage} damage. Current health: {self.current_health}")


class Archer(Character):
    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height, speed)
        self.attack_damage = 8
        self.defense = 3
        self.max_health = 80
        self.current_health = self.max_health

    def take_damage(self, damage):
        """Reduces the character's health by the damage amount."""
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
        print(f"Archer took {damage} damage. Current health: {self.current_health}")


class Mage(Character):
    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height, speed)
        self.attack_damage = 5
        self.defense = 2
        self.max_health = 70
        self.current_health = self.max_health
        self.max_mana = 100
        self.current_mana = self.max_mana

    def take_damage(self, damage):
        """Reduces the character's health by the damage amount."""
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
        print(f"Mage took {damage} damage. Current health: {self.current_health}")

    def use_mana(self, mana_cost):
        """Reduces the character's mana by the mana cost."""
        self.current_mana -= mana_cost
        print(f"Mage used {mana_cost} mana. Current mana: {self.current_mana}")
