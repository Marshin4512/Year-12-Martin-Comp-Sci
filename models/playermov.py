import pygame
from player import Player

class PlayerController:

    #Initilise everything
    def __init__(self):
        self.player = Player(pygame.Rect(25, 25, 30, 30), speed=5)
        self.move_x = 0
        self.move_y = 0
    

    def handle_event(self, event):
        #Handle the arrow key movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.move_y = -5
            elif event.key == pygame.K_DOWN:
                self.move_y = 5
            elif event.key == pygame.K_LEFT:
                self.move_x = -5
            elif event.key == pygame.K_RIGHT:
                self.move_x = 5
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                self.move_y = 0
            elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.move_x = 0

    def update(self, wall_rects):
        #update player poisiton
        self.player.move(self.move_x, self.move_y, wall_rects)
        
        


    def draw(self, screen):
        #draw player
        self.player.draw(screen)
    
    def reset(self, position):
        #reset player to position
        self.player.reset()
        self.player.sprite.topleft = position
        self.move_x = 0
        self.move_y = 0
        
