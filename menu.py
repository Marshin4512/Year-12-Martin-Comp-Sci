# menu.py
import pygame
import sys
from config import WINWIDTH, WINHEIGHT, WHITE, BLACK

class menu:
    def terminate(self):
        pygame.quit()
        sys.exit()

    def start_menu(self, screen):
        font = pygame.font.Font(None, 74)
        text = font.render("Press ENTER to Start", True, WHITE)
        text_rect = text.get_rect(center=(WINWIDTH // 2, WINHEIGHT // 2))
        while True:
            screen.fill(BLACK)
            screen.blit(text, text_rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return