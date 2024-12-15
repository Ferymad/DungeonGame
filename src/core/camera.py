class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0

    def update(self, target_x, target_y):
        self.x = target_x - self.width // 2
        self.y = target_y - self.height // 2

    def apply(self, rect):
        if isinstance(rect, pygame.Rect):
            return pygame.Rect(rect.x - self.x, rect.y - self.y, rect.width, rect.height)
        else:
            x, y = rect
            return (x - self.x, y - self.y)
