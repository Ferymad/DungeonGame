import pygame
from core import settings
from entities.player import Warrior
from entities.enemy import Enemy
from map.tile_renderer import TileRenderer
from core.camera import Camera
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Warrior(100, 100, 32, 32, 2)
        self.camera = Camera(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        self.tile_renderer = TileRenderer()
        self.tiles = []
        self.enemies = []
        self.attacks = []
        self.projectiles = []
        self.generate_map()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(settings.FPS)
        self.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.player.handle_input(event, self.tiles)

    def update(self):
        self.camera.update(self.player.x, self.player.y)
        for enemy in self.enemies:
            enemy.move(self.tiles)

        # Handle player attacks
        attack = self.player.attack()
        if attack:
            self.attacks.append(attack)

        # Handle player spells
        projectile = self.player.cast_spell(pygame.mouse.get_pos())
        if projectile:
            self.projectiles.append(projectile)

        # Update projectiles
        for projectile in self.projectiles:
            projectile.update()

        # Check for attack collisions
        for attack in self.attacks:
            for enemy in self.enemies:
                if attack.check_collision(enemy.hitbox):
                    enemy.take_damage(attack.damage)
                    self.attacks.remove(attack)
                    break

        # Check for projectile collisions
        for projectile in self.projectiles:
            for enemy in self.enemies:
                if projectile.check_collision(enemy.hitbox):
                    enemy.take_damage(projectile.damage)
                    self.projectiles.remove(projectile)
                    break

        # Remove dead enemies
        self.enemies = [enemy for enemy in self.enemies if enemy.health > 0]

    def generate_map(self):
        from map.generator import MapGenerator
        difficulty_level = 1
        generator = MapGenerator(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, 6, 10, difficulty_level, 5, 15)
        self.tiles = generator.generate_map()
        self.enemies = self.create_enemies()

    def create_enemies(self):
        enemies = []
        for room in self.get_floor_rooms():
            if random.random() < 0.5:
                x = room.center_x * 16
                y = room.center_y * 16
                enemy = Enemy(x, y, 32, 32, 1, 50)
                enemies.append(enemy)
        return enemies

    def get_floor_rooms(self):
        floor_rooms = []
        for room in self.tiles:
            if room.type == "floor":
                floor_rooms.append(room)
        return floor_rooms

    def render(self):
        self.screen.fill(settings.BG_COLOR)
        self.tile_renderer.render(self.screen, self.tiles, self.camera)
        pygame.draw.rect(self.screen, (255, 255, 255), self.camera.apply(self.player.hitbox))
        for enemy in self.enemies:
            pygame.draw.rect(self.screen, (255, 0, 0), self.camera.apply(enemy.hitbox))
        for attack in self.attacks:
            pygame.draw.rect(self.screen, (255, 255, 0), self.camera.apply(attack.hitbox))
        for projectile in self.projectiles:
            pygame.draw.rect(self.screen, (0, 255, 255), self.camera.apply(projectile.hitbox))
        pygame.display.flip()

    def quit(self):
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
