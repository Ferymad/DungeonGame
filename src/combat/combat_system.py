import pygame
import random
from src.combat.status_effect import StatusEffect

class CombatSystem:
    def __init__(self):
        self.attack_cooldowns = {}
        self.default_cooldown = 500  # milliseconds
        self.defense = 0  # Default defense
        self.critical_hit_chance = 0.1  # 10% chance
        self.dodge_chance = 0.1  # 10% chance
        self.block_chance = 0.2  # 20% chance
        self.block_damage_reduction = 0.5  # Reduce damage by 50%
        self.critical_hit_multiplier = 2  # Double damage on crit

        self.status_effects = {}  # Dictionary to store status effects on targets

    def handle_attack(self, attacker, target, attack, attack_type="melee", status_effect=None):
        """Handles attacks, including cooldown checks."""
        if self.is_attack_on_cooldown(attacker, attack_type):
            print(f"{attacker}'s {attack_type} attack is on cooldown!")
            return False
        else:            
            if random.random() < self.dodge_chance:
                print(f"{target} dodges the attack!")
                self.reset_cooldown(attacker, attack_type)
                return False

            damage = self.calculate_damage(attack.damage)
            if random.random() < self.block_chance:
                damage *= self.block_damage_reduction
                print(f"{target} blocks the attack, reducing damage to {damage}!")

            if random.random() < self.critical_hit_chance:
                damage *= self.critical_hit_multiplier
                print(f"Critical Hit!")
            print(f"{attacker} performs a {attack_type} attack on {target} for {damage} damage!")

            if status_effect:
                self.apply_status_effect(target, status_effect)
            self.reset_cooldown(attacker, attack_type)
            return True

    def calculate_damage(self, attack_damage):
        """Calculates the damage dealt after defense."""
        damage = attack_damage - self.defense
        if damage < 0:
            damage = 0
        return damage

    def apply_status_effect(self, target, status_effect):
        """Applies a status effect to a target."""
        if target not in self.status_effects:
            self.status_effects[target] = []
        self.status_effects[target].append(status_effect)
        print(f"{target} is affected by {status_effect.effect_type} for {status_effect.duration} ms.")

    def remove_status_effect(self, target, status_effect):
        """Removes a status effect from a target."""
        if target in self.status_effects and status_effect in self.status_effects[target]:
            self.status_effects[target].remove(status_effect)
            print(f"{target} is no longer affected by {status_effect.effect_type}.")

    def update_status_effects(self, delta_time):
        """Updates all active status effects."""
        for target, effects in list(self.status_effects.items()):
            for effect in list(effects):
                effect.update(delta_time)
                if effect.is_expired():
                    self.remove_status_effect(target, effect)
                elif effect.effect_type == "poison":
                    damage = self.calculate_damage(effect.magnitude)
                    print(f"{target} takes {damage} poison damage.")
                    target.take_damage(damage)

    def is_attack_on_cooldown(self, attacker, attack_type):
        """Checks if an attack is on cooldown."""
        last_attack_time = self.attack_cooldowns.get((attacker, attack_type), 0)
        return pygame.time.get_ticks() - last_attack_time < self.default_cooldown

    def reset_cooldown(self, attacker, attack_type):
        """Resets the cooldown for an attack."""
        self.attack_cooldowns[(attacker, attack_type)] = pygame.time.get_ticks()
