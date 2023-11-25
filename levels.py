import random
import pygame

from bloque import Bloque
from obstacle import ProyectilEnemigo

width, height = 800, 600


class Nivel:
    def __init__(self, fondo, blocks, velocidad_proyectiles, enemycant, ratio):
        bloques = pygame.sprite.Group()
        proyectiles_enemigos = pygame.sprite.Group()
        self.fondo = fondo
        self.bloques = bloques
        self.enemycant = enemycant
        self.ratio = ratio
        for i in range(blocks):
            x = random.randint(100, width - 200)
            y = random.randint(100, height - 100)
            self.velocidad_proyectiles = velocidad_proyectiles
            bloque = Bloque(x, y, 'bloque.png', velocidad_proyectiles)
            bloques.add(bloque)

        

