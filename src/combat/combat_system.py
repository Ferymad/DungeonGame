import pygame

class CombatSystem:
    def __init__(self):
        self.attack_cooldowns = {}
        self.default_cooldown = 500  # milliseconds
        self.defense = 0 # Default defense

    def handle_attack(self, attacker, target, attack_type="melee"):
        """Handles attacks, including cooldown checks."""
        if self.is_attack_on_cooldown(attacker, attack_type):
            print(f"{attacker}'s {attack_type} attack is on cooldown!")
            return False
        else:
            damage = self.calculate_damage(attack.damage)
            print(f"{attacker} performs a {attack_type} attack on {target} for {damage} damage!")
            self.reset_cooldown(attacker, attack_type)
            return True

    def calculate_damage(self, attack_damage):
        """Calculates the damage dealt after defense."""
        damage = attack_damage - self.defense
        if damage < 0:
            damage = 0
        return damage

    def is_attack_on_cooldown(self, attacker, attack_type):
        """Checks if an attack is on cooldown."""
        last_attack_time = self.attack_cooldowns.get((attacker, attack_type), 0)
        return pygame.time.get_ticks() - last_attack_time < self.default_cooldown

    def reset_cooldown(self, attacker, attack_type):
        """Resets the cooldown for an attack."""
        self.attack_cooldowns[(attacker, attack_type)] = pygame.time.get_ticks()
