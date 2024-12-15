import pygame
from src.core import settings
from src.entities.player import Warrior
from src.map.tile_renderer import TileRenderer
from src.core.camera import Camera

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(-1, 0, self.tiles)
                if event.key == pygame.K_RIGHT:
                    self.player.move(1, 0, self.tiles)
                if event.key == pygame.K_UP:
                    self.player.move(0, -1, self.tiles)
                if event.key == pygame.K_DOWN:
                    self.player.move(0, 1, self.tiles)

    def update(self):
        self.camera.update(self.player.x, self.player.y)

    def generate_map(self):
        from src.map.generator import MapGenerator
        difficulty_level = 1
        generator = MapGenerator(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, 6, 10, difficulty_level, 5, 15)
        self.tiles = generator.generate_map()

    def render(self):
        self.screen.fill(settings.BG_COLOR)
        self.generate_map()
        self.tile_renderer.render(self.screen, self.tiles, self.camera)
        pygame.draw.rect(self.screen, (255, 255, 255), self.camera.apply(self.player.hitbox))
        pygame.display.flip()

    def quit(self):
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
