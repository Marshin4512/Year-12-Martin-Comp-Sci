import pygame
from level import Level
from levelone import maze as level_one_maze, cell_size as level_one_cell_size
from leveltwo import maze as level_two_maze, cell_size as level_two_cell_size
from walls import *

class LevelManager:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.current_level = None
        self.current_level_number = 0
        self.level_data = [
            {
                'maze': level_one_maze,
                'cell_size': level_one_cell_size,
                'player_start': (50, 50),
                'enemy_start': (100, 50),
                'player_size': (30, 30),
                'player_speed': 4
            },
            {
                'maze': level_two_maze,
                'cell_size': level_two_cell_size,
                'player_start': (12, 12),
                'enemy_start': (50, 50),
                'player_size': (5, 5),
                'player_speed': 1
            }
        ]
     
    def load_level(self, level_number):
        """Load a specific level by number (1-based)"""
        if 1 <= level_number <= len(self.level_data):
            self.current_level_number = level_number
            level_config = self.level_data[level_number - 1]
            
            # Update player attributes for this level
            self.player.sprite.width = level_config['player_size'][0]
            self.player.sprite.height = level_config['player_size'][1]
            self.player.speed = level_config['player_speed']
            
            # Create and load the level
            if self.current_level:
                self.current_level.clear()
                
            self.current_level = Level(
                maze=level_config['maze'],
                cell_size=level_config['cell_size'],
                player=self.player,
                screen=self.screen
            )
            self.current_level.load()
            
            self.current_level.wall_manager.load_coins()
            
            return True
        return False

    def load_next_level(self):
        """Load the next level in sequence"""
        next_level = self.current_level_number + 1
        if next_level <= len(self.level_data):
            self.load_level(next_level)
            return True
        return False  # No more levels

    def get_player_start_pos(self):
        """Get the player starting position for the current level"""
        return self.level_data[self.current_level_number - 1]['player_start']
    
    def get_enemy_start_pos(self):
        """Get the enemy starting position for the current level"""
        return self.level_data[self.current_level_number - 1]['enemy_start']

    def draw(self):
        """Draw the current level"""
        if self.current_level:
            self.current_level.draw()
