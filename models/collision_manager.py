import pygame
from enemy_manager import *
from walls import *
class CollisionManager:
    #Inistlise everything
    def __init__(self, level_manager, player_controller, enemy_manager):
        self.level_manager = level_manager
        self.player_controller = player_controller
        self.enemy_manager = enemy_manager
        self.coins_collected = 0

    def check_collisions(self):
       
        if not self.level_manager.current_level:
            return False

        player = self.player_controller.player
        current_level = self.level_manager.current_level
        
        # Check for end tile collision (level completion)
        if current_level.check_end_collision():
            return True

        # Check coin collisions
        self.check_coin_collisions()
        
        # Check enemy collisions
        self.check_enemy_collisions()
        
        return False
    
    def check_coin_collisions(self):
        #Check if coin has collided with player
        player = self.player_controller.player
        current_level = self.level_manager.current_level
        wall_manager = current_level.wall_manager
        
        # Use a copy to remove item
        coins_to_remove = []
        
        for coin_rect in wall_manager.coin_rects:
            if player.sprite.colliderect(coin_rect):
                coins_to_remove.append(coin_rect)
                self.coins_collected += 1
                
        
        # Remove collected coins
        for coin in coins_to_remove:
            wall_manager.coin_rects.remove(coin)
            
    
    def check_enemy_collisions(self):
            #Check if enemy has touched player
            player = self.player_controller.player

            for enemy in self.enemy_manager.enemies:
             if player.sprite.colliderect(enemy.sprite):
                # Reset player position
                self.player_controller.reset(self.level_manager.get_player_start_pos())
                
                # Reset the colliding enemy's position
                enemy.reset()
                break