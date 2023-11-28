import pygame

width, height = 800, 600
class Bloque(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen_bloque, blockspeed):
        super().__init__()
        self.image = pygame.image.load(imagen_bloque)
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = x - 50
        self.rect.y = y - 100
        
        self.velocidad = blockspeed
        self.cayendo = False
        self.destruido = False
        self.contador_destruidos = 0  

    def update(self):
        if self.cayendo:
            self.rect.y += self.velocidad
            if self.rect.top > height:
                self.destruido = True
                self.contador_destruidos += 1  # Incrementa el contador cuando el bloque sale de la pantalla