import pygame
import colores
import sqlite3
from constantes import *

with sqlite3.connect("data.db") as conexion:
                 #### crear la tabla ####
                try:
                    sentencia = ''' create table jugador
                        (
                        id integer primary key autoincrement,
                        name text,
                        score real
                        )
                        ''' 
                    conexion.execute(sentencia)
                    print("Se creo la tabla jugador")
                except sqlite3.OperationalError:
                    print("La tabla jugador ya existe")

pygame.init()


imagen=pygame.image.load("menu\\nombre.png") 
imagen= pygame.transform.scale(imagen,(ALTO_VENTANA,ANCHO_VENTANA))

fuente= pygame.font.SysFont("arias",50) 
ingreso=""
ingreso_rect= pygame.Rect(215,370,200,50)

pantalla=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("menu principal")

cuadro_texto_activo = False
bandera=True
while bandera: 
        lista=  pygame.event.get()  
        for evento in lista: 
            if evento.type == pygame.QUIT: 
                bandera= False 
                pygame.quit() 
            if evento.type == pygame.KEYDOWN: 
                if evento.key == pygame.K_BACKSPACE: 
                    ingreso = ingreso[0:-1] 
                elif evento.key == pygame.K_RETURN: 
                    nombre_jugador= ingreso 
                    with sqlite3.connect("data.db") as conexion: 
                        conexion.execute("INSERT INTO jugador (name, score) VALUES (?, 0)", (nombre_jugador,))
                        conexion.commit()
                        print("Nombre del jugador ", ingreso)
                    import principal 
                else:
                    ingreso += evento.unicode 

        pantalla.blit(imagen,(0,0)) 
        pygame.draw.rect(pantalla,colores.MAGENTA,ingreso_rect) 
        font_input_surface=fuente.render(ingreso,True,colores.YELLOW1)
        pantalla.blit(font_input_surface,(ingreso_rect.x + 5, ingreso_rect.y + 5))

        pygame.display.flip()
        pygame.display.update()