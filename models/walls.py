
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

    def load_end(self):
    # Separate storage for end tiles
        self.end_rects = []
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
             if self.maze[row][col] == 2:  # End tile
                rect = pygame.Rect(
                    col * self.cell_size,
                    row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                self.end_rects.append(rect)

    def draw_walls(self, screen):
    # Draw walls in black
      for wall in self.wall_rects:
        pygame.draw.rect(screen, (0, 0, 0), wall)

    def draw_end(self, screen):
    # Draw end tiles in green
        for end in self.end_rects:
            pygame.draw.rect(screen, (0, 255, 0), end)