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
        #datos.sort(reverse=True)
        for i in range(len(datos)):
            for j in range(len(datos)-1):
                if  datos[i][2]>datos[j][2] :
                    aux=datos[i]
                    datos[i]=datos[j]
                    datos[j]=aux 
    except Exception:
        print("Error")

bandera=True
while bandera: 
    pantalla.blit(imagen,(0,0)) 
    y=375
    for  fila in datos:
        scores="{0}        {1}".format(fila[1],fila[2])
        score = fuente.render(scores, True, colores.YELLOW1) 
        if y<500:
            pantalla.blit(score, (150,y))  
        y +=25 
    lista = pygame.event.get() 
    for evento in lista: 
        if evento.type == pygame.QUIT: 
            bandera = False 
        elif evento.type == pygame.KEYDOWN: 
            if evento.key == pygame.K_RETURN: 
                import menu 
    pantalla.blit(texto, (50, 550))
    pantalla.blit(dato, (150, 340))  
    pygame.display.flip()
pygame.quit()
