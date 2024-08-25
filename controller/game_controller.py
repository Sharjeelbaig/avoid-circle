import pygame
import sys

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            while not self.model.check_collision():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.model.move_box("left")
                if keys[pygame.K_RIGHT]:
                    self.model.move_box("right")

                self.model.add_circle()
                self.model.move_circles()

                self.view.draw()
                self.clock.tick(30)

            # Handle game over and retry logic
            retry_rect = self.view.display_game_over()
            self.handle_retry(retry_rect)

    def handle_retry(self, retry_rect):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if retry_rect.collidepoint(event.pos):
                        self.reset_game()
                        return  # Restart the game loop

    def reset_game(self):
        # Reset the game state to start a new game
        self.model.box_x = self.model.width // 2 - self.model.box_width // 2
        self.model.circles = []
        self.model.score = 0
