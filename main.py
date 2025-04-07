import sys
import pygame
from game import Game

def main(): #This is the main file

    try:
        # Create game instance
        game = Game()
        
        # Run the game
        game.run()
        
    except KeyboardInterrupt:
        #Exception handling, if interuppted,g ame is terminated
        print("Game terminated")
        pygame.quit()
        sys.exit(0)
        
    except Exception as e:
        # Handle unexpected errors, if there is error, print error, and terminate the game
        print(f"Error: {e}")
        pygame.quit()
        sys.exit(1)
        
    finally:
        # Ensure pygame is shut down
        pygame.quit()

if __name__ == "__main__":
    main()