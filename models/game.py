import pygame
import sys
from config import FPS, WINWIDTH, WINHEIGHT, WHITE
from level_manager import LevelManager
from player import *
from enemy_manager import EnemyManager
from collision_manager import CollisionManager
from menu import Menu
from playermov import *
class Game:
    def __init__(self):
        self.FPS = FPS
        self.screen = None
        self.clock = None
        self.running = True
        
        # Initialize managers
        self.level_manager = None
        self.player_controller = None
        self.enemy_manager = None
        self.collision_manager = None
        self.menu = None

    def initialize(self):
        """Initialize pygame and all game components"""
        pygame.init()
        self.screen = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
        pygame.display.set_caption("Puzzle Maze")
        self.clock = pygame.time.Clock()
        
        # Initialize managers
        self.menu = Menu()
        self.player_controller = PlayerController()
        self.level_manager = LevelManager(self.screen, self.player_controller.player)
        self.enemy_manager = EnemyManager()
        self.collision_manager = CollisionManager(
            self.level_manager,
            self.player_controller,
            self.enemy_manager
        )

    def handle_events(self):
        """Process user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.player_controller.handle_event(event)

    def update(self):
        """Update game state"""
        # Update player position based on current input
        self.player_controller.update(self.level_manager.current_level.wall_manager.wall_rects)
        
        # Update enemies
        self.enemy_manager.update(self.player_controller.player)
        
        # Check collisions
        level_complete = self.collision_manager.check_collisions()
        
        # Handle level transitions
        if level_complete:
            self.level_manager.load_next_level()
            self.player_controller.reset(self.level_manager.get_player_start_pos())
            self.enemy_manager.reset(self.level_manager.get_enemy_start_pos())

    def render(self):
        """Render the current game state"""
        self.screen.fill(WHITE)
        
        # Draw level
        self.level_manager.draw()
        
        # Draw player
        self.player_controller.draw(self.screen)
        
        # Draw enemies
        self.enemy_manager.draw(self.screen)
        
        pygame.display.flip()

    def terminate(self):
        """Shut down the game"""
        pygame.quit()
        sys.exit()

    def run(self):
        """Main game loop"""
        self.initialize()
        self.menu.start_menu(self.screen)
        self.level_manager.load_level(1)  # Start with level 1
        self.player_controller.reset(self.level_manager.get_player_start_pos())
        self.enemy_manager.add_enemy(self.level_manager.get_enemy_start_pos())

        # Main game loop
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.FPS)

        self.terminate()
