import pygame

width, height = 800, 600
class Vidas(pygame.sprite.Sprite):
    def __init__(self, total_vidas):
        super().__init__()

        self.total_vidas = total_vidas
        self.vidas_restantes = total_vidas
        self.font = pygame.font.Font('freesansbold.ttf', 18)
        self.vida_text = self.font.render("Lifes:", True, (255, 255, 255))
        self.vida_text_rect = self.vida_text.get_rect(center=(width - 150, height - 550))
        
        self.vida_images = [pygame.image.load('corazon.png') for _ in range(self.total_vidas)]
        self.vida_rects = [image.get_rect(topleft=(width - 180 + i * 30, 80)) for i, image in enumerate(self.vida_images)]

    def perder_vida(self, screen):
        
        if self.vidas_restantes > 0:
            self.vidas_restantes -= 1
            self.vida_images.pop()
            self.vida_rects = [image.get_rect(topleft=(width - 180 + i * 30, 80)) for i, image in enumerate(self.vida_images)]


        