import pygame
import colores
import sqlite3 
import os

ANCHO_VENTANA = 600
ALTO_VENTANA = 600

pygame.init()
imagen = pygame.image.load("menu\\score.png") 
imagen = pygame.transform.scale(imagen, (ALTO_VENTANA, ANCHO_VENTANA))

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("menu principal") 

ruta_fuente = os.path.join('mega pixel', 'C:\\programacion I\\turbo revolution\\mega pixel\\00TT.TTF')
fuente = pygame.font.Font(ruta_fuente, 30)

texto = fuente.render("press enter to return to the menu", True, colores.YELLOW1)  
dato = fuente.render("nombres  tiempos  puntajes", True, colores.YELLOW1)  

datos_db = []  # Variable para almacenar los datos de la base de datos

with sqlite3.connect("data.db") as conexion: 
    try: 
        cursor = conexion.execute("SELECT * FROM jugador")
        datos_db = cursor.fetchall()
    except Exception as e: 
        print("Error:", e) 

bandera = True
while bandera: 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                import menu 
    
    pantalla.blit(imagen, (0, 0))
    pantalla.blit(texto, (50, 550))
    pantalla.blit(dato, (100, 340))

    for i, fila in enumerate(datos_db):
        fila_renderizada = fuente.render(str(fila), True, colores.YELLOW1) 
        pantalla.blit(fila_renderizada, (100, 375))

    pygame.display.flip()

pygame.quit()

