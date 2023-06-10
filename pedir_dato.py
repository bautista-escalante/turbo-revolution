import pygame
import colores
import sqlite3

ANCHO_VENTANA=600  
ALTO_VENTANA=600 
with sqlite3.connect("data.db") as conexion:
                 #### crear la tabla ####
                try:
                    sentencia = ''' create table jugador
                        (
                        id integer primary key autoincrement,
                        name text,
                        time real,
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

font_input= pygame.font.SysFont("arias",50)
ingreso=""
ingreso_rect= pygame.Rect(215,370,200,50)

pantalla=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("menu principal")

bandera=True
while bandera: 
        lista=  pygame.event.get()
        for evento in lista:
            if evento.type == pygame.QUIT:
                bandera= False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[0:-1]
                else:
                    ingreso = ingreso + evento.unicode


        pantalla.blit(imagen,(0,0)) 
        pygame.draw.rect(pantalla,colores.MAGENTA,ingreso_rect,2) 
        font_input_surface=font_input.render(ingreso,True,colores.MAGENTA)
        pantalla.blit(font_input_surface,(200,400))
        pygame.draw.rect(pantalla,colores.MAGENTA,ingreso_rect) 
        
        if ingreso != "": 
            nombre_jugador =" pepe"
            with sqlite3.connect("data.db") as conexion:
                #### insertar datos ##### 
                conexion.execute("insert into jugador(name,time,score)"
                "values (?,?,?)", (nombre_jugador, 0,0)) 
            try:
                conexion.commit()# Actualiza los datos realmente en la tabla
            except Exception:
                print("Error") 
            import principal

        pygame.display.flip()
pygame.quit()


    


        