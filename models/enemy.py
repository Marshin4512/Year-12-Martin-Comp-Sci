from entity import Entity

class Enemy(Entity):
    """Enemy entity that inherits from Entity"""
    
    def __init__(self, sprite, speed, chase_range=200):
        super().__init__(sprite, speed, color="RED")
        self.chase_range = chase_range
    
    def chase(self, target):
        if self.sprite.x < target.sprite.x:
            self.sprite.x += self.speed
        elif self.sprite.x > target.sprite.x:
            self.sprite.x -= self.speed

        if self.sprite.y < target.sprite.y:
            self.sprite.y += self.speed
        elif self.sprite.y > target.sprite.y:
            self.sprite.y -= self.speed

    