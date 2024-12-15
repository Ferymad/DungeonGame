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
        self.last_attack_time = 0
        self.attack_cooldown = 500 # milliseconds

    def handle_input(self, event, tiles):
        """Handles keyboard input and updates character position."""
        dx = 0
        dy = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            if event.key == pygame.K_RIGHT:
                dx = 1
            if event.key == pygame.K_UP:
                dy = -1
            if event.key == pygame.K_DOWN:
                dy = 1
            if event.key == pygame.K_SPACE:
                self.attack()
        self.move(dx, dy, tiles)

    def move(self, dx, dy, tiles):
        """Moves the character by dx and dy, checking for collisions."""
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed
        new_hitbox = pygame.Rect(new_x, new_y, self.width, self.height)

        if not self.check_collision(new_hitbox, tiles):
            self.x = new_x
            self.y = new_y
            self.hitbox.x = self.x
            self.hitbox.y = self.y

    def check_collision(self, rect, tiles):
        """Checks if the character's rectangle collides with any tile."""
        for tile in tiles:
            if tile.type != "floor":
                continue
            tile_rect = pygame.Rect(tile.x * 16, tile.y * 16, 16, 16) # Assuming tile size is 16x16
            if rect.colliderect(tile_rect):
                return True
        return False

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

    def attack(self):
        """Performs a melee attack."""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time > self.attack_cooldown:
            attack_x = self.x + self.width
            attack_y = self.y
            attack_width = 20
            attack_height = self.height
            self.last_attack_time = current_time
            return MeleeAttack(self, attack_x, attack_y, attack_width, attack_height, 10)
        return None


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

