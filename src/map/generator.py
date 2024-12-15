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
        self.boss_room = None
        self.treasure_rooms = []

    def generate_map(self):
        self.rooms = []
        self.tiles = []
        self.boss_room = None
        self.treasure_rooms = []
        self._bsp_split(0, 0, self.map_width, self.map_height)
        self._create_corridors()
        self._designate_special_rooms()
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

    def _create_corridors(self):
        for i in range(len(self.rooms) - 1):
            room1 = self.rooms[i]
            room2 = self.rooms[i+1]
            self._create_corridor(room1, room2)

    def _create_corridor(self, room1, room2):
        x1, y1 = room1.center_x, room1.center_y
        x2, y2 = room2.center_x, room2.center_y

        while x1 != x2:
            x1 += 1 if x1 < x2 else -1
            self.tiles.append(Tile(x1, y1, "floor"))
        while y1 != y2:
            y1 += 1 if y1 < y2 else -1
            self.tiles.append(Tile(x1, y1, "floor"))

    def _designate_special_rooms(self):
        if not self.rooms:
            return

        # Designate boss room (last room for now)
        self.boss_room = self.rooms[-1]
        for tile in self.tiles:
            if tile.x >= self.boss_room.x and tile.x < self.boss_room.x + self.boss_room.width and tile.y >= self.boss_room.y and tile.y < self.boss_room.y + self.boss_room.height:
                tile.tile_type = "boss"

        # Designate treasure rooms (random rooms, not the boss room)
        num_treasure_rooms = min(3, len(self.rooms) - 1)  # Ensure we don't pick the boss room
        if num_treasure_rooms > 0:
            treasure_room_candidates = self.rooms[:-1]
            self.treasure_rooms = random.sample(treasure_room_candidates, num_treasure_rooms)
            for room in self.treasure_rooms:
                for tile in self.tiles:
                    if tile.x >= room.x and tile.x < room.x + room.width and tile.y >= room.y and tile.y < room.y + room.height:
                        tile.tile_type = "treasure"
