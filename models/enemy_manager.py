import pygame
from enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []

    def add_enemy(self, position, speed=1):
        #crate enemy at the position
        enemy = Enemy(
            pygame.Rect(position[0], position[1], 20, 20), 
            speed=speed
        )
        self.enemies.append(enemy)
        return enemy

    def update(self, player):
        #update enemy
        for enemy in self.enemies:
            enemy.chase(player)

    def draw(self, screen):
        #draw enemy
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def reset(self, position):
        #reset enemey position
        if not self.enemies:
            self.add_enemy(position)
        else:
            for enemy in self.enemies:
                enemy.sprite.topleft = position
