import pygame
import os
from bloque import Bloque

from proyectil import Proyectil


# Configuración de la pantalla
width, height = 640, 600

# Obtener la ruta del directorio actual del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta relativa de la carpeta donde se encuentran los frames
frames_folder = os.path.join(script_dir, "Player")

proyectiles = pygame.sprite.Group()

class Protagonista(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        frame_filename = os.path.join(frames_folder, "pixil-frame-1.png")
        self.image = pygame.image.load(frame_filename)
        self.image = pygame.transform.scale(self.image, (115, 115))

        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.centery = height - 75
        
        self.velocidad = 5

        self.shoot_delay = 200  # Tiempo de espera entre disparos en milisegundos
        self.last_shot = pygame.time.get_ticks()

    def update(self, keys):

        if keys[pygame.K_LEFT]:
            self.rect.x = max(0, self.rect.x - self.velocidad)
        if keys[pygame.K_RIGHT]:
            self.rect.x = min(width - self.rect.width, self.rect.x + self.velocidad)
        if keys[pygame.K_UP]:
            self.rect.y = max(0, self.rect.y - self.velocidad)
        if keys[pygame.K_DOWN]:
            self.rect.y = min(height - self.rect.height, self.rect.y + self.velocidad)

        """if keys[pygame.K_z]:  # Disparar solo si no hay un proyectil en vuelo
            self.disparar()"""
        
        if keys[pygame.K_LSHIFT]:
            self.velocidad = 1
        else:
            self.velocidad = 5
        
        #colisiones = pygame.sprite.spritecollide(self, bloques, True)
        
        # Verificar colisiones entre proyectiles y bloques y destruirlos
        
        

    def disparar(self, proyectiles):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            proyectil = Proyectil(self.rect.centerx, self.rect.top)
            proyectiles.add(proyectil)
            self.last_shot = now
