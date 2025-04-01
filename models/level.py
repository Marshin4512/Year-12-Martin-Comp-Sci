import pygame
from walls import WallManager

class Level:
    def __init__(self, maze, cell_size, player, screen):
        self.maze = maze
        self.cell_size = cell_size
        self.wall_manager = WallManager(maze, cell_size)
        self.player = player
        self.screen = screen

    def load(self):
        # Load walls and end tiles
        self.wall_manager.load_walls()
        self.wall_manager.load_end()

    def reset_player_position(self, start_position):
        # Reset the player to the starting position
        self.player.sprite.topleft = start_position

    def clear(self):
        # Clear all elements from the screen
        self.wall_manager.wall_rects.clear()
        self.wall_manager.end_rects.clear()

    def draw(self):
        # Draw walls and end tiles
        self.wall_manager.draw_walls(self.screen)
        self.wall_manager.draw_end(self.screen)

    def check_end_collision(self):
        # Check if the player collides with the end tiles
        for end_rect in self.wall_manager.end_rects:
            if self.player.sprite.colliderect(end_rect):
                return True
        return False