import pygame

width, height = 800, 600
class VictoriaScreen:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 36)
        self.text = self.font.render("¡Victoria!", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(width // 2, height // 2))

    def mostrar(self, screen):
        screen.blit(self.text, self.text_rect)
        pygame.display.flip()
