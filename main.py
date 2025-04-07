import sys
import pygame
from game import Game

def main():
    

    try:
        # Create game instance
        game = Game()
        
        # Run the game
        game.run()
        
    except KeyboardInterrupt:
        #exit
        print("Game terminated")
        pygame.quit()
        sys.exit(0)
        
    except Exception as e:
        # Handle unexpected errors
        print(f"Error: {e}")
        pygame.quit()
        sys.exit(1)
        
    finally:
        # Ensure pygame is shut down
        pygame.quit()

if __name__ == "__main__":
    main()