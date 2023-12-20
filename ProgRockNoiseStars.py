""" 
ProgRockNoiseStars is a vertical shooter game
Copyright (C) 2023 Jaime Alexander Martinez Paiz

"""
import random
import pygame
import sys
import math
import os
from levels import Nivel
from lifes import Vidas
from obstacle import ProyectilEnemigo

from protagonista import Protagonista
from proyectil import Proyectil
from bloque import Bloque
from gameover import GameOverScreen
from successlevel import VictoriaScreen
#---------------------------------------------// SISTEMA BASICO DEL JUEGO //---------------------------------------------------


# Inicializar pygame
pygame.init()
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

# Definir colores
white = (255, 255, 255)
black = (0, 0, 0)
RED = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Progressive Gun")
icon = pygame.image.load("Logo Game.png")
icon = pygame.transform.scale(icon, (68, 68))
pygame.display.set_icon(icon)

#----------------------------------- Niveles----------------------------
niveles = [
    Nivel("Door2.png", 10, 5, 200, 3),
    Nivel("Door3.png", 20, 7, 170, 3),
    Nivel("Door4.png", 30, 8, 170, 3),
    Nivel("Door5.png", 40, 10, 120, 5),
    # Agrega más niveles según sea necesario
]
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
victoria_screen = VictoriaScreen()
proyectiles_enemigos = pygame.sprite.Group()


#------------------------------------------------// MENU DEL JUEGO //-----------------------------------------------------
# Variables de juego 
game_started = False
pausa = False
contador_bloques_destruidos = 0
configurando = False

# Función para mostrar la imagen de pausa
def mostrar_pausa():
    global pausa
    # Cargar la imagen de pausa
    imagen_pausa = pygame.image.load("Pause.png")
    imagen_pausa = pygame.transform.scale(imagen_pausa, (width, height))
    pygame.mixer.music.pause()
    def draw_button(text, x, y, width, height, button_color, text_color):
        pygame.draw.rect(screen, button_color, (x, y, width, height))
        button_text = fontObj.render(text, True, text_color)
        text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
        screen.blit(button_text, text_rect)
        
    while pausa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 100 <= mouse_x <= 300 and 300 <= mouse_y <= 350:
                    pausa = False  # Salir del bucle de configuración
    
    screen.blit(imagen_pausa, (0, 0))
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
                if 290 <= mouse_x <= 510 and 390 <= mouse_y <= 430:
                    menu_running = False  # Salir del bucle de menú
                    pygame.mixer.music.stop()
                    global game_started
                    game_started = True
                elif 290 <= mouse_x <= 510 and 450 <= mouse_y <= 490:
                    global configurando
                    configurando = True  # Iniciar configuración
                    configuracion_juego()  # Llamar a la función de configuración
                elif 290 <= mouse_x <= 510 and 510 <= mouse_y <= 550:
                    pygame.quit()  # Salir del juego
                    
        # Mostrar la imagen de fondo del menú
        screen.blit(menu_bg, (0, 0))
        screen.blit(imageImg, (imagex, imagey))
        # Dibujar el botón
        draw_button("INICIAR", 290, 390, 220, 40, (0, 128, 255), white)
        draw_button("CONFIGURAR", 290, 450, 220, 40, (0, 128, 255), white)
        draw_button("SALIR", 290, 510, 220, 40, (0, 128, 255), white)
        pygame.display.flip()

def configuracion_juego():
    menu_bg = pygame.image.load("menu.png")
    menu_bg = pygame.transform.scale(menu_bg, (width, height))
    global configurando
    
    def draw_button(text, x, y, width, height, button_color, text_color):
        pygame.draw.rect(screen, button_color, (x, y, width, height))
        button_text = fontObj.render(text, True, text_color)
        text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
        screen.blit(button_text, text_rect)
    
    while configurando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 300 <= mouse_x <= 500 and 500 <= mouse_y <= 550:
                    configurando = False  # Salir del bucle de configuración

        screen.blit(menu_bg, (0, 0))
        # Lógica de configuración
        # Muestra elementos de configuración (pueden ser entradas de usuario, opciones, etc.)
        # Dibuja el botón para regresar al menú principal
        draw_button("REGRESAR AL MENÚ", 300, 500, 200, 50, (0, 128, 255), white)

        pygame.display.flip()


# Llamar a la función de menú de inicio
menu_inicio()
nivel_actual = 0
canciones = ['01.MP3', '02.MP3', '03.MP3', '04.MP3']  # Ajusta la lista según tus necesidades
musicas = [pygame.mixer.Sound(cancion) for cancion in canciones]

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
            
            #pygame.mixer.music.stop()  # Detener la música actual

            # Cargar la música del nivel actual
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(canciones[nivel_actual])
                pygame.mixer.music.play(1)
            
            # Resto de la lógica del juego
            bloques = niveles[nivel_actual].bloques
            enemycant = niveles[nivel_actual].enemycant
            ratio = niveles[nivel_actual].ratio
            velocidad_proyectiles = niveles[nivel_actual].velocidad_proyectiles
            bg_img = pygame.image.load(niveles[nivel_actual].fondo)
            bg_img = pygame.transform.scale(bg_img, (width - 200, height - -100))        
            
            screen.blit(bg_img, (0, 0))
            screen.blit(status_img, (600, 0))
            
            protagonista.update(keys, screen)
            screen.blit(protagonista.image, (protagonista.rect.x, protagonista.rect.y))
            
            proyectiles.update()  # Actualizar el grupo de proyectiles
            proyectiles.draw(screen)  # Dibujar los proyectiles en la pantalla
            
            bloques = pygame.sprite.Group([bloque for bloque in bloques if not bloque.destruido])
            
            bloques.update()
            bloques.draw(screen)
            
            
            if nivel_actual == 0:
                if random.randint(0, enemycant) < ratio:  # Ajusta el porcentaje según la frecuencia deseada
                    proyectil_enemigo = ProyectilEnemigo(random.randint(0, width - 200), 0)
                    proyectiles_enemigos.add(proyectil_enemigo)
            elif nivel_actual == 1:
                if random.randint(0, enemycant) < ratio:  # Ajusta el porcentaje según la frecuencia deseada
                    proyectil_enemigo = ProyectilEnemigo(0, random.randint(0, height))
                    proyectiles_enemigos.add(proyectil_enemigo)
            if nivel_actual == 2:
                if random.randint(0, enemycant) < ratio:  # Ajusta el porcentaje según la frecuencia deseada
                    proyectil_enemigo = ProyectilEnemigo(random.randint(0, width - 200), 0)
                    proyectiles_enemigos.add(proyectil_enemigo)
                    proyectil_enemigo = ProyectilEnemigo(0, random.randint(0, height))
                    proyectiles_enemigos.add(proyectil_enemigo)
            if nivel_actual == 3:
                if random.randint(0, enemycant) < ratio:  # Ajusta el porcentaje según la frecuencia deseada
                    proyectil_enemigo = ProyectilEnemigo(random.randint(0, width - 200), 0)
                    proyectiles_enemigos.add(proyectil_enemigo)
                
            proyectiles_enemigos.update(nivel_actual)
            proyectiles_enemigos.draw(screen)
            
            for bloque in bloques:
                if bloque.destruido:
                    bloques.remove(bloque)  # Elimina el bloque de la lista
                    contador_bloques_destruidos += 1  # Incrementa el contador global
            
            # Elimina proyectiles que están fuera de la pantalla
            proyectiles = pygame.sprite.Group([proyectil for proyectil in proyectiles if proyectil.rect.bottom >= 0])
            colisiones_proyectiles_bloques = pygame.sprite.groupcollide(proyectiles, bloques, True, False)
            

            for proyectil, bloques_colisionados in colisiones_proyectiles_bloques.items():
                for bloque in bloques_colisionados:
                    # Activa la caída para el bloque
                    bloque.cayendo = True

            protagonista.deadend(bloques, proyectiles_enemigos, screen)
            
            if not (bloques):
                nivel_actual += 1  # Avanzar al siguiente nivel
                pygame.mixer.music.stop()

                # Verificar si hay más niveles o si el juego ha terminado
                if nivel_actual < len(niveles):
                    # Configurar el siguiente nivel
                    bloques = niveles[nivel_actual].bloques
                    enemycant = niveles[nivel_actual].enemycant
                    ratio = niveles[nivel_actual].ratio
                    velocidad_proyectiles = niveles[nivel_actual].velocidad_proyectiles
                    bg_img = pygame.image.load(niveles[nivel_actual].fondo)
                    bg_img = pygame.transform.scale(bg_img, (width - 200, height - -100))
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.load(canciones[nivel_actual])
                        pygame.mixer.music.play(1)
                        
                else:
                    # El juego ha terminado, puedes mostrar una pantalla de victoria o reiniciar niveles
                    nivel_actual = 0
                    victoria_screen.mostrar(screen)
                    pygame.time.delay(1000)
                    pygame.quit()
                    sys.exit()
                
                victoria_screen.mostrar(screen)
                pygame.time.delay(1000)  # Pausa por 3 segundos 
            
            pygame.mixer.music.unpause()
            clock.tick(FPS)
            pygame.display.flip()

pygame.display.update()
#clock.tick(30)
# Salir
pygame.quit()
sys.exit()
