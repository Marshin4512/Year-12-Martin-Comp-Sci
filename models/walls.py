import pygame

class WallManager:
    #Initilise everything
    def __init__(self, maze, cell_size):
        self.wall_rects = []
        self.end_rects = []
        self.coin_rects = []  # Add this for coins
        self.cell_size = cell_size
        self.maze = maze

    def load_walls(self):
        #Create a wall for the value 1
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == 1:  # Wall tile
                    rect = pygame.Rect(
                        col * self.cell_size,
                        row * self.cell_size,
                        self.cell_size,
                        self.cell_size
                    )
                    self.wall_rects.append(rect)

    def load_end(self):
        #Create a end for the value 2
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == 2:  # End tile
                    rect = pygame.Rect(
                        col * self.cell_size,
                        row * self.cell_size,
                        self.cell_size,
                        self.cell_size
                    )
                    self.end_rects.append(rect)

    def load_coins(self): 
        #Create a coin for the value 3
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == 3:  
                    rect = pygame.Rect(
                        col * self.cell_size,
                        row * self.cell_size,
                        self.cell_size,
                        self.cell_size
                    )
                    self.coin_rects.append(rect)
                print("coin loaded")

    def draw_walls(self, screen):
        #draw the wall
        for wall in self.wall_rects:
            pygame.draw.rect(screen, (0, 0, 0), wall)  

    def draw_end(self, screen):
        #draw the end
        for end in self.end_rects:
            pygame.draw.rect(screen, (0, 255, 0), end)  

    def draw_coins(self, screen):  
        #draw the coin
        for coin in self.coin_rects:
            pygame.draw.rect(screen, (255, 255, 0), coin) 
            print("yello  coin")
  