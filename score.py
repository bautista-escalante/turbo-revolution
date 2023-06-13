import pygame
import colores
import sqlite3 

ANCHO_VENTANA=600
ALTO_VENTANA=600

pygame.init()
imagen=pygame.image.load("menu\\score.png") 
imagen= pygame.transform.scale(imagen,(ALTO_VENTANA,ANCHO_VENTANA))

pantalla=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("menu principal")

fuente= pygame.font.SysFont("georgia",30) 
texto = fuente.render("press enter to return to the menu",True,colores.WHITE)  
datos = fuente.render("nombres||tiempos||puntajes",True,colores.WHITE)  
with sqlite3.connect("data.db") as conexion: 
    try: 
        #### imprimir en pantalla #### 
        cursor=conexion.execute("SELECT * FROM jugador")
        for fila in cursor:
            print(fila)
    except Exception: 
        print("Error") 

bandera=True
while bandera: 
    pantalla.blit(imagen,(0,0)) 
    ##### puntajes #### 
    score = fuente.render("pepe",True,colores.WHITE)
    lista = pygame.event.get()
    for evento in lista:
        if evento.type == pygame.QUIT:
            bandera= False
        elif evento.type == pygame.KEYDOWN :
            if evento.key == pygame.K_RETURN:
                import menu 
    pantalla.blit(texto,(50,550))
    pantalla.blit(datos,(100,340))
    pantalla.blit(score,(100,390))
    pygame.display.flip()
pygame.quit()
