import pygame

class Character:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.max_health = 100
        self.current_health = self.max_health
        self.max_mana = 100
        self.current_mana = self.max_mana
        self.max_stamina = 100
        self.current_stamina = self.max_stamina
        self.experience = 0

    def move(self, dx, dy):
        """Moves the character by dx and dy."""
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.hitbox.x = self.x
        self.hitbox.y = self.y

    def get_hitbox(self):
        """Returns the character's hitbox."""
        return self.hitbox
    
    def take_damage(self, damage):
        """Reduces the character's health by the damage amount."""
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
        print(f"{self.__class__.__name__} took {damage} damage. Current health: {self.current_health}")

    def use_mana(self, mana_cost):
        """Reduces the character's mana by the mana cost."""
        self.current_mana -= mana_cost
        print(f"{self.__class__.__name__} used {mana_cost} mana. Current mana: {self.current_mana}")

    def gain_experience(self, amount):
        """Increases the character's experience points."""
        self.experience += amount
        print(f"{self.__class__.__name__} gained {amount} experience. Total experience: {self.experience}")


class Warrior(Character):
    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height, speed)
        self.attack_damage = 10
        self.defense = 5

    def take_damage(self, damage):
        """Reduces the character's health by the damage amount."""
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0


class Archer(Character):
    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height, speed)
        self.attack_damage = 8
        self.defense = 3

    def take_damage(self, damage):
        """Reduces the character's health by the damage amount."""
        self.current_health -= damage


class Mage(Character):
    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height, speed)
        self.attack_damage = 5
        self.defense = 2

    def take_damage(self, damage):
        """Reduces the character's health by the damage amount."""
        self.current_health -= damage

