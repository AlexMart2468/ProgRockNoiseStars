import pygame

class Bloque(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen_bloque):
        super().__init__()
        self.image = pygame.image.load(imagen_bloque)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x - 50
        self.rect.y = y - 100
        
        self.velocidad = 20
        self.cayendo = False

    def update(self):
        # Lógica de actualización del bloque (si es necesario)
       #pass
    
    #def strike(self):
        if self.cayendo:
            self.rect.y += self.velocidad