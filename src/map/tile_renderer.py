import pygame
import os
from src.core import settings

class TileRenderer:
    def __init__(self):
        self.tile_images = {
            "floor": pygame.Surface((16, 16)),
            "treasure": pygame.Surface((16, 16)),
            "boss": pygame.Surface((16, 16)),
        }
    import pygame
    import os

    class TileRenderer:
        def __init__(self):
            self.tile_images = {
                "floor": self.load_image("floor.png"),
                "treasure": self.load_image("treasure.png"),
                "boss": self.load_image("boss.png"),
            }

        def load_image(self, filename):
            """Loads an image from the assets/tiles directory."""
            filepath = os.path.join("src", "assets", "tiles", filename)
            try:
                image = pygame.image.load(filepath)
                return image
            except pygame.error as e:
                print(f"Error loading image {filename}: {e}")
                return None

        def render(self, screen, tiles, camera):
            for tile in tiles:
                image = self.tile_images.get(tile.type)
                if image:
                    screen.blit(image, camera.apply((tile.x * 16, tile.y * 16)))
