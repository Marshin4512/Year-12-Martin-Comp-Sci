import pygame
import sys
from config import WINWIDTH, WINHEIGHT, WHITE, BLACK

class Menu:
  

    def start_menu(self, screen): #Menu function
        
        font = pygame.font.Font(None, 74)#Font
        text = font.render("Press ENTER to Start", True, WHITE) #Appearance of menu
        text_rect = text.get_rect(center=(WINWIDTH // 2, WINHEIGHT // 2)) # Size
        #While loop is there to handle stuff
        while True:
            screen.fill(BLACK)
            screen.blit(text, text_rect)
            pygame.display.flip()
            for event in pygame.event.get(): # If quit = quite
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.KEYDOWN: #If certain key is pressed return
                    if event.key == pygame.K_RETURN:
                        return
