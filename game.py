"""
This is the test main loop for testing the game engine.
"""
from core.wrwengine import WrwGameEngine

def main():
    """
    This function is the game loop
    """
    se = WrwGameEngine()

    se.start_game()

if __name__ == "__main__":
    main()
