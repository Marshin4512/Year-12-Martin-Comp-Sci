import pygame

class Entity:
    """Base class for all game entities"""
    
    def __init__(self, sprite, speed, color="WHITE"):
        self.sprite = sprite
        self.speed = speed
        self.color = color
        self.initial_position = sprite.topleft
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.sprite)
    
    def move(self, x_change, y_change, obstacles=None):
        """Base movement method with collision detection"""
        # Apply speed multiplier
        x_change *= self.speed
        y_change *= self.speed
        
        if obstacles is None:
            obstacles = []
        
        # Move on X axis first and check collision
        new_x_position = self.sprite.move(x_change, 0)
        if not any(new_x_position.colliderect(obstacle) for obstacle in obstacles):
            self.sprite.x = new_x_position.x
        
        # Then move on Y axis and check collision
        new_y_position = self.sprite.move(0, y_change)
        if not any(new_y_position.colliderect(obstacle) for obstacle in obstacles):
            self.sprite.y = new_y_position.y
    
    def reset(self):
        """Reset entity to its initial position"""
        self.sprite.topleft = self.initial_position