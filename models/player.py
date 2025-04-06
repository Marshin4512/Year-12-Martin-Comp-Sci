from entity import Entity

class Player(Entity):
    """Player entity that inherits from Entity"""
    
    def __init__(self, sprite, speed):
        super().__init__(sprite, speed, color="BLUE")
        self.coins_collected = 0
    
    def collect_coin(self):
        """Action when player collects a coin"""
        self.coins_collected += 1
        return self.coins_collected 

    