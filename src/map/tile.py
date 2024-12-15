class Tile:
    def __init__(self, x, y, tile_type):
        self.x = x
        self.y = y
        self.type = tile_type

    def __repr__(self):
        return f"Tile(x={self.x}, y={self.y}, type='{self.type}')"
