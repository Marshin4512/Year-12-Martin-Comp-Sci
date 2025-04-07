from entity import Entity

class Enemy(Entity): #Enemy inherits from the entity class
#initlises everything
    def __init__(self, sprite, speed):
        super().__init__(sprite, speed, color="RED")
        
    
    def chase(self, target): #Handles the chasing, if it is not touching it then move towards player
        if self.sprite.x < target.sprite.x:
            self.sprite.x += self.speed
        elif self.sprite.x > target.sprite.x:
            self.sprite.x -= self.speed

        if self.sprite.y < target.sprite.y:
            self.sprite.y += self.speed
        elif self.sprite.y > target.sprite.y:
            self.sprite.y -= self.speed

    