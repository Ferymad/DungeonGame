import pygame
from src.core import settings

class TileRenderer:
    def __init__(self):
        self.tile_images = {
            "floor": pygame.Surface((16, 16)),
            "treasure": pygame.Surface((16, 16)),
            "boss": pygame.Surface((16, 16)),
        }
        self.tile_images["floor"].fill((200, 200, 200))
        self.tile_images["treasure"].fill((0, 255, 0))
        self.tile_images["boss"].fill((255, 0, 0))

    def render(self, screen, tiles, camera):
        for tile in tiles:
            image = self.tile_images.get(tile.type)
            if image:
                screen.blit(image, camera.apply((tile.x * 16, tile.y * 16)))
