import random
from src.core import settings
from src.map.tile import Tile

class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.center_x = x + width // 2
        self.center_y = y + height // 2

class MapGenerator:
    def __init__(self, map_width, map_height, min_room_size, max_room_size):
        self.map_width = map_width
        self.map_height = map_height
        self.min_room_size = min_room_size
        self.max_room_size = max_room_size
        self.rooms = []
        self.tiles = []

    def generate_map(self):
        self.rooms = []
        self.tiles = []
        self._bsp_split(0, 0, self.map_width, self.map_height)
        self._create_corridors()
        return self.tiles

    def _bsp_split(self, x, y, width, height):
        if width < self.min_room_size or height < self.min_room_size:
            # Create a room if the area is small enough
            self._create_room(x, y, width, height)
            return

        split_horizontal = random.choice([True, False])

        if split_horizontal:
            split_point = random.randint(self.min_room_size, width - self.min_room_size)
            self._bsp_split(x, y, split_point, height)
            self._bsp_split(x + split_point, y, width - split_point, height)
        else:
            split_point = random.randint(self.min_room_size, height - self.min_room_size)
            self._bsp_split(x, y, width, split_point)
            self._bsp_split(x, y + split_point, width, height - split_point)

    def _create_room(self, x, y, width, height):
        # Create a room within the rectangle
        room_x = random.randint(x + 1, x + width - self.min_room_size)
        room_y = random.randint(y + 1, y + height - self.min_room_size)
        room_width = random.randint(self.min_room_size, min(width - 2, self.max_room_size))
        room_height = random.randint(self.min_room_size, min(height - 2, self.max_room_size))

        room = Room(room_x, room_y, room_width, room_height)
        self.rooms.append(room)
        for tile_x in range(room.x, room.x + room.width):
            for tile_y in range(room.y, room.y + room.height):
                self.tiles.append(Tile(tile_x, tile_y, "floor"))
