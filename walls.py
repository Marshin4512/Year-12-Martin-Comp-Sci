
import pygame

class WallManager:
    def __init__(self, maze, cell_size):
        self.wall_rects = []
        self.cell_size = cell_size
        self.maze = maze

    def load_walls(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == 1:  # Wall tile
                    rect = pygame.Rect(
                        col * self.cell_size,
                        row * self.cell_size,
                        self.cell_size,
                        self.cell_size
                    )
                    self.wall_rects.append(rect)

    def draw_walls(self, screen):
        for wall in self.wall_rects:
            pygame.draw.rect(screen, (0, 0, 0), wall)