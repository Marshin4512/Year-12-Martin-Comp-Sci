from entity import Entity

class Player(Entity):#Player inherits from entity class
   
    
    def __init__(self, sprite, speed):
        #Initislisation
        super().__init__(sprite, speed, color="BLUE")
        self.coins_collected = 0
    


    