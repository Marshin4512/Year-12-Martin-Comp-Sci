# main.py
import pygame
import sys
from config import WINWIDTH, WINHEIGHT, FPS, WHITE
from levelone import maze, cell_size
from player import player
from menu import menu
from walls import WallManager

class Game:
    def __init__(self):
        self.FPS = FPS
        self.screen = None
        self.clock = None
        self.player = player(pygame.Rect(50, 50, 30, 30))
        self.wall_manager = WallManager(maze, cell_size)
        self.menu = menu()

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
        pygame.display.set_caption("Puzzle Maze")
        self.clock = pygame.time.Clock()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def main(self):
        self.initialize()
        self.menu.start_menu(self.screen)
        self.wall_manager.load_walls()

        running = True
        move_x, move_y = 0, 0

        while running:
            self.screen.fill(WHITE)
            self.wall_manager.draw_walls(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        move_y = -5
                    elif event.key == pygame.K_DOWN:
                        move_y = 5
                    elif event.key == pygame.K_LEFT:
                        move_x = -5
                    elif event.key == pygame.K_RIGHT:
                        move_x = 5
                elif event.type == pygame.KEYUP:
                    if event.key in (pygame.K_UP, pygame.K_DOWN):
                        move_y = 0
                    elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                        move_x = 0

            self.player.move(move_x, move_y, self.wall_manager.wall_rects)
            self.player.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.FPS)


if __name__ == "__main__":
    Game().main()