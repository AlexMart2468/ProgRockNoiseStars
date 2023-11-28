""" 
ProgRockNoiseStars is a vertical shooter game
Copyright (C) 2023 Jaime Alexander Martinez Paiz

"""
import random
import pygame
import sys
import math
import os

from protagonista import Protagonista
from proyectil import Proyectil
from bloque import Bloque
from gameover import GameOverScreen
#---------------------------------------------// SISTEMA BASICO DEL JUEGO //---------------------------------------------------


# Inicializar pygame
pygame.init()
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

# Definir colores
white = (255, 255, 255)
black = (0, 0, 0)
RED = (255, 0 , 0)
green = (0, 255, 0)#]
blue = (0, 0, 255)

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Progressive Gun")
icon = pygame.image.load('Logo Game.png')
icon = pygame.transform.scale(icon, (68, 68))
#icon_tarea = pygame.image.load('Alt_Logo.ico')
#icon_tarea = pygame.transform.scale(icon_tarea, (32, 32))
pygame.display.set_icon(icon)

# Cargar la imagen de fondo
bg_img = pygame.image.load("Door2.png")
bg_img = pygame.transform.scale(bg_img, (width - 200, height - -100))
screen = pygame.display.set_mode((800, 600))
status_img = pygame.image.load("Status.png")
status_img = pygame.transform.scale(status_img, (200, height))

# Cargar la música
file = 'Menu.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)
pygame.mixer.init()
            

# Reloj del sistema y FPS
clock = pygame.time.Clock()
FPS = 60

# Configuración de texto
fontObj = pygame.font.Font('freesansbold.ttf', 32)

#-----------------------------------------------// CLASES PARA SPRITES // ---------------------------------------------
# En el bucle de inicialización del juego
protagonista = Protagonista()
proyectiles = pygame.sprite.Group()
bloques = pygame.sprite.Group()

# Crear bloques aleatorios
for i in range(30):
    x = random.randint(100, width - 200)
    y = random.randint(100, height - 100)
    bloque = Bloque(x, y, 'bloque.png')
    bloques.add(bloque)


#------------------------------------------------// MENU DEL JUEGO //-----------------------------------------------------
# Variables de juego 
game_started = False
pausa = False

# Función para mostrar la imagen de pausa
def mostrar_pausa():
    # Cargar la imagen de pausa
    imagen_pausa = pygame.image.load("Pause.png")
    imagen_pausa = pygame.transform.scale(imagen_pausa, (width, height))
    screen.blit(imagen_pausa, (0, 0))
    pygame.mixer.music.pause()
    def draw_button(text, x, y, width, height, button_color, text_color):
        pygame.draw.rect(screen, button_color, (x, y, width, height))
        button_text = fontObj.render(text, True, text_color)
        text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
        screen.blit(button_text, text_rect)
    
    # Dibujar el botón
    draw_button("RETURN", 100, 300, 200, 50, (0, 128, 255), white)
    pygame.display.flip()

def menu_inicio():
    # Cargar imagen de fondo del menú
    menu_bg = pygame.image.load("menu.png")
    menu_bg = pygame.transform.scale(menu_bg, (width, height))
    
    imageImg = pygame.image.load('Title.png')
    imageImg = pygame.transform.scale(imageImg, (680, 380))
    imagex = 75
    imagey = 25

    def draw_button(text, x, y, width, height, button_color, text_color):
        pygame.draw.rect(screen, button_color, (x, y, width, height))
        button_text = fontObj.render(text, True, text_color)
        text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
        screen.blit(button_text, text_rect)
        
    # Bucle de menú
    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Verificar si se hizo clic en el botón
                if 300 <= mouse_x <= 500 and 400 <= mouse_y <= 450:
                    menu_running = False  # Salir del bucle de menú
                    pygame.mixer.music.stop()
                    global game_started
                    game_started = True
                elif 300 <= mouse_x <= 500 and 500 <= mouse_y <= 550:
                    pygame.quit()  # Salir del juego
                    
        # Mostrar la imagen de fondo del menú
        screen.blit(menu_bg, (0, 0))
        screen.blit(imageImg, (imagex, imagey))
        # Dibujar el botón
        draw_button("INICIAR", 300, 400, 200, 50, (0, 128, 255), white)
        draw_button("SALIR", 300, 500, 200, 50, (0, 128, 255), white)
        pygame.display.flip()

# Llamar a la función de menú de inicio
menu_inicio()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pausa = not pausa
                if pausa:
                    mostrar_pausa()
                else:
                    screen.fill((0, 0, 0))
            elif event.key == pygame.K_z:
                protagonista.disparar(proyectiles)
    if game_started:
        if not pausa:
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_q]:
                quit()
            

            protagonista.update(keys)
            # Resto de la lógica del juego
            screen.blit(bg_img, (0, 0))
            screen.blit(status_img, (600, 0))
            screen.blit(protagonista.image, (protagonista.rect.x, protagonista.rect.y))
            
            
            
            proyectiles.update()  # Actualizar el grupo de proyectiles
            proyectiles.draw(screen)  # Dibujar los proyectiles en la pantalla
            bloques.update()
            bloques.draw(screen)
            # Elimina proyectiles que están fuera de la pantalla
            proyectiles = pygame.sprite.Group([proyectil for proyectil in proyectiles if proyectil.rect.bottom >= 0])
            
            #colisiones_proyectiles = pygame.sprite.groupcollide(proyectiles, bloques, True, True)
            colisiones_proyectiles_bloques = pygame.sprite.groupcollide(proyectiles, bloques, True, False)
            colisiones_protagonista_bloques_cayendo = pygame.sprite.spritecollide(protagonista, bloques, False)

            for proyectil, bloques_colisionados in colisiones_proyectiles_bloques.items():
                for bloque in bloques_colisionados:
                    # Activa la caída para el bloque
                    bloque.cayendo = True

            protagonista.deadend(bloques)
            pygame.mixer.music.unpause()
            clock.tick(FPS)
            pygame.display.flip()

pygame.display.update()
#clock.tick(30)
# Salir
pygame.quit()
sys.exit()
