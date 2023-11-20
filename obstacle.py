# Agregar esta clase en tu código
import pygame
import os

width, height = 800, 600
# Obtener la ruta del directorio actual del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta relativa de la carpeta donde se encuentran los frames
frames_folder = os.path.join(script_dir, "Bullet")

class ProyectilEnemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        frame_filename = os.path.join(frames_folder, "enemybullet.png")
        self.image = pygame.image.load(frame_filename)
        self.image = pygame.transform.scale(self.image, (15, 15))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y

        self.speed_y = 3

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > height:
            self.kill()
