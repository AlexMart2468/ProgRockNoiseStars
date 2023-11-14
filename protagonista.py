import sys
import pygame
import os
from bloque import Bloque
from gameover import GameOverScreen
from lifes import Vidas

from proyectil import Proyectil


# Configuración de la pantalla
width, height = 600, 600

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
        self.image = pygame.transform.scale(self.image, (45, 55))

        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.centery = height - 75
        
        self.velocidad = 5

        self.vidas = Vidas(3)  # Inicializa el contador de vidas

        
        self.shoot_delay = 200  # Tiempo de espera entre disparos en milisegundos
        self.last_shot = pygame.time.get_ticks()

    def update(self, keys, screen):
        #self.vidas.draw(screen)

        if keys[pygame.K_LEFT]:
            self.rect.x = max(0, self.rect.x - self.velocidad)
        if keys[pygame.K_RIGHT]:
            self.rect.x = min(width - self.rect.width, self.rect.x + self.velocidad)
        if keys[pygame.K_UP]:
            self.rect.y = max(0, self.rect.y - self.velocidad)
        if keys[pygame.K_DOWN]:
            self.rect.y = min(height - self.rect.height, self.rect.y + self.velocidad)

        if keys[pygame.K_LSHIFT]:
            self.velocidad = 1
        else:
            self.velocidad = 5
        
    def disparar(self, proyectiles):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            proyectil = Proyectil(self.rect.centerx, self.rect.top)
            proyectiles.add(proyectil)
            self.last_shot = now
    
    def deadend(self, bloques, screen):
        screen.blit(self.vidas.vida_text, self.vidas.vida_text_rect)
        for rect, image in zip(self.vidas.vida_rects, self.vidas.vida_images):
            screen.blit(image, rect)
        colisiones_bloques_cayendo = pygame.sprite.spritecollide(self, bloques, True)
        if colisiones_bloques_cayendo:
            self.vidas.perder_vida(screen)
            if self.vidas.vidas_restantes <= 0:
                # Mostrar la pantalla de Game Over
                game_over_screen = GameOverScreen()
                game_over_screen.mostrar()
                pygame.time.delay(3000)  # Pausa por 3 segundos
                pygame.quit()
                sys.exit()
            