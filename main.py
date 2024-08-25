# main.py

import pygame
from model.game_model import GameModel
from view.game_view import GameView
from controller.game_controller import GameController

def main():
    pygame.init()
    
    pygame.display.set_caption("Avoid Circles")
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    # Initialize MVC components
    model = GameModel(WIDTH, HEIGHT, box_width=100, box_height=20, circle_radius=20)
    view = GameView(model, screen)
    controller = GameController(model, view)
    
    # Run the game
    controller.run()

if __name__ == "__main__":
    main()
