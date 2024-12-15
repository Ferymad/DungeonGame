class StatusEffect:
    def __init__(self, effect_type, duration, magnitude):
        self.effect_type = effect_type
        self.duration = duration
        self.magnitude = magnitude
        self.timer = 0

    def update(self, delta_time):
        """Updates the status effect timer."""
        self.timer += delta_time

    def is_expired(self):
        """Checks if the status effect has expired."""
        return self.timer >= self.duration
