import pygame

class Player:
    def __init__(self, sprite, speed):  
        self.sprite = sprite
        self.speed = speed

    def draw(self, screen):
        pygame.draw.rect(screen, "BLUE", self.sprite)

    def move(self, x_change, y_change, wall_rects):
        x_change *= self.speed
        y_change *= self.speed

        # Calculate new position
        new_position = self.sprite.move(x_change, y_change)

        # Update position only if no collision
        if not any(new_position.colliderect(wall) for wall in wall_rects):
            self.sprite = new_position