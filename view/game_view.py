# view/game_view.py

import pygame

class GameView:
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.colors = {
            "blue": (0, 0, 255),
            "red": (255, 0, 0),
            "black": (0, 0, 0),
            "white": (255, 255, 255),
        }

        # Load the background image
        self.background = pygame.image.load("assets/background.png").convert()
        self.background = pygame.transform.scale(self.background, (model.width, model.height))
        
    def draw(self):
        # self.screen.fill(self.colors["black"])
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen, self.colors["blue"], (self.model.box_x, self.model.box_y, self.model.box_width, self.model.box_height))
        for circle in self.model.circles:
            pygame.draw.circle(self.screen, self.colors["red"], circle, self.model.circle_radius)
        
        # Draw the score
        score_text = self.font.render(f'Score: {self.model.score}', True, self.colors["white"])
        self.screen.blit(score_text, (10, 10))  # Position the score at the top-left corner


        pygame.display.flip()

    def display_game_over(self):
        self.screen.fill(self.colors["black"])
        score_text = self.font.render(f'Score: {self.model.score}', True, self.colors["white"])
        game_over_text = self.font.render('Game Over', True, self.colors["white"])
        retry_text = self.font.render('Retry', True, self.colors["white"])
        game_over_rect = game_over_text.get_rect(center=(self.model.width // 2, self.model.height // 2 - 50))
        retry_rect = retry_text.get_rect(center=(self.model.width // 2, self.model.height // 2 + 50))
        score_text_rect = score_text.get_rect(center=(self.model.width // 2, self.model.height // 2 - 100))
        self.screen.blit(score_text, score_text_rect)
        
        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(retry_text, retry_rect)
        pygame.display.flip()
        return retry_rect
