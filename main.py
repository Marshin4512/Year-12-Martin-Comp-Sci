import pygame
import sys
from config import WINWIDTH, WINHEIGHT, FPS, WHITE
from levelone import maze as level_one_maze, cell_size as level_one_cell_size
from leveltwo import maze as level_two_maze, cell_size as level_two_cell_size
from playermod import Player
from menu import menu
from level import *
from walls import WallManager
from enemy import Enemy

class Game:
    def __init__(self):
        self.FPS = FPS
        self.screen = None
        self.clock = None
        self.player = Player(pygame.Rect(50, 50, 30, 30), speed=4)  # Update here
        self.enemy = Enemy(pygame.Rect(100, 50, 30, 30), speed=1)
        self.current_level = None
        self.menu = menu()

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
        pygame.display.set_caption("Puzzle Maze")
        self.clock = pygame.time.Clock()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def load_level_one(self):
        # Initialize level 1
        self.current_level = Level(
            maze=level_one_maze,
            cell_size=level_one_cell_size,
            player=self.player,
            screen=self.screen
        )
        self.current_level.load()
        self.current_level.reset_player_position((50, 50))

    def load_level_two(self,screen):
        
        self.current_level.clear()
        screen.fill((255,255,255))
        self.player = Player(pygame.Rect(20, 20, 10, 10), speed=4)
        
        self.current_level = Level(
            maze=level_two_maze,
            cell_size=level_two_cell_size,
            player=self.player,
            screen=self.screen
        )
        self.current_level.load()
        

    def main(self):
        self.initialize()
        self.menu.start_menu(self.screen)
        self.load_level_one()  # Start with level 1

        running = True
        move_x, move_y = 0, 0

        while running:
            self.screen.fill(WHITE)
            self.current_level.draw()

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

            self.player.move(move_x, move_y, self.current_level.wall_manager.wall_rects)
            self.player.draw(self.screen)
            self.enemy.chase(self.player)
            self.enemy.draw(self.screen)

            # Check for end tile collision
            if self.current_level.check_end_collision():
                print("Loading next level...")

                # Transition to level 2
                self.load_level_two(screen="WHITE")

            pygame.display.flip()
            self.clock.tick(self.FPS)

        self.terminate()

if __name__ == "__main__":
    Game().main()