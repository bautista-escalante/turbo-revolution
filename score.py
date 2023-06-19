import pygame
import os
import colores
import sqlite3 

ANCHO_VENTANA=600
ALTO_VENTANA=600 

pygame.init()
imagen=pygame.image.load("menu\\score.png")  
imagen= pygame.transform.scale(imagen,(ALTO_VENTANA,ANCHO_VENTANA))

pantalla=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("menu principal") 

ruta_fuente = os.path.join('mega pixel', 'C:\\programacion I\\turbo revolution\\mega pixel\\00TT.TTF')
fuente = pygame.font.Font(ruta_fuente, 30)

texto = fuente.render("press enter to return to the menu", True, colores.YELLOW1)  
dato = fuente.render("nombres  puntajes", True, colores.YELLOW1)  

with sqlite3.connect("data.db") as conexion: 
    try: 
        #### imprimir en pantalla #### 
        cursor=conexion.execute("SELECT * FROM jugador")
        datos = cursor.fetchall()
        for i in datos:
            lista=lista(i)    
    except Exception: 
        print("Error") 

bandera=True
while bandera: 
    pantalla.blit(imagen,(0,0)) 
    for  fila in datos: 
        dato = fuente.render(str(fila), True, colores.YELLOW1) 
        pantalla.blit(dato, (100,375)) 
    ##### puntajes #### 
    score = fuente.render("", True, colores.YELLOW1)
    lista = pygame.event.get()
    for evento in lista:
        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                import menu 
    pantalla.blit(texto, (50, 550))
    pantalla.blit(dato, (100, 340)) 
    pantalla.blit(score, (100, 390))
    pygame.display.flip()
pygame.quit()
