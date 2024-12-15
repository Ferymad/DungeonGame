from src.combat.attack import Projectile

class Spell:
    def __init__(self, name, mana_cost, effect):
        self.name = name
        self.mana_cost = mana_cost
        self.effect = effect

    def apply_effect(self, caster, target):
        """Applies the spell's effect."""
        print(f"{caster} casts {self.name} on {target}!")
        # Implement actual spell effect here

class ProjectileSpell(Spell):
    def __init__(self, name, mana_cost, projectile_speed, projectile_damage, projectile_width, projectile_height):
        super().__init__(name, mana_cost, "projectile")
        self.projectile_speed = projectile_speed
        self.projectile_damage = projectile_damage
        self.projectile_width = projectile_width
        self.projectile_height = projectile_height

    def cast(self, caster, x, y, target_x, target_y):
        """Creates and returns a projectile."""
        velocity_x = target_x - x
        velocity_y = target_y - y
        # Normalize the velocity vector
        magnitude = (velocity_x**2 + velocity_y**2)**0.5
        if magnitude > 0:
            velocity_x /= magnitude
            velocity_y /= magnitude
        velocity_x *= self.projectile_speed
        velocity_y *= self.projectile_speed
        projectile = Projectile(caster, x, y, velocity_x, velocity_y, self.projectile_width, self.projectile_height, self.projectile_damage)
        return projectile
