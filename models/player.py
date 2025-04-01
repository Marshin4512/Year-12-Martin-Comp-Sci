import pygame
class player:
    def __init__(self, sprite):
        self.sprite = sprite

    def draw(self, screen):
        pygame.draw.rect(screen, "BLUE", self.sprite)

    def move(self, x_change, y_change, wall_rects):

        new_position = self.sprite.move(x_change, y_change)
        

        if not any(new_position.colliderect(wall) for wall in wall_rects):
            # Update position only if no collision, THIS IS HOW IT WORKS MARTIN
            self.sprite = new_position
