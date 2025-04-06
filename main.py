import sys
import pygame
from game import Game

def main():
    
    """Entry point for the game
    
    Creates and runs the game instance with error handling
    """
    try:
        # Create game instance
        game = Game()
        
        # Run the game
        game.run()
        
    except KeyboardInterrupt:
        # Handle clean exit with Ctrl+C
        print("Game terminated by user")
        pygame.quit()
        sys.exit(0)
        
    except Exception as e:
        # Handle unexpected errors
        print(f"Error: {e}")
        pygame.quit()
        sys.exit(1)
        
    finally:
        # Ensure pygame is properly shut down in any case
        pygame.quit()

if __name__ == "__main__":
    main()