import pygame
from src.core import settings

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

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

    def update(self):
        pass

    def test_map_generation(self):
        from src.map.generator import MapGenerator
        difficulty_level = 1
        for i in range(3):
            generator = MapGenerator(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, 6, 10, difficulty_level, 5, 15)
            tiles = generator.generate_map()
            for tile in tiles:
                if tile.tile_type == "floor":
                    pygame.draw.rect(self.screen, (255, 255, 255), (tile.x, tile.y, 1, 1))
                elif tile.tile_type == "treasure":
                    pygame.draw.rect(self.screen, (0, 255, 0), (tile.x, tile.y, 1, 1))
                elif tile.tile_type == "boss":
                    pygame.draw.rect(self.screen, (255, 0, 0), (tile.x, tile.y, 1, 1))
            difficulty_level += 1
            pygame.display.flip()
            pygame.time.wait(1000)
            self.screen.fill(settings.BG_COLOR)

    def render(self):
        self.screen.fill(settings.BG_COLOR)
        self.test_map_generation()
        pygame.display.flip()

    def quit(self):
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
