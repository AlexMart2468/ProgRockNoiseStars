# gameover.py
import pygame

class GameOverScreen:
    def __init__(self):
        width, height = 800, 600
        self.screen = pygame.display.set_mode((width, height))
        self.background_color = (0, 0, 0)
        self.font = pygame.font.Font('freesansbold.ttf', 64)
        self.game_over_text = self.font.render("Game Over", True, (255, 0, 0))
        self.game_over_rect = self.game_over_text.get_rect(center=(width // 2, height // 2))

    def mostrar(self):
        self.screen.fill(self.background_color)
        self.screen.blit(self.game_over_text, self.game_over_rect)
        pygame.display.flip()
