# turbo_revolution
segundo parcial laboratorio 

# jugabilidad
* nuestro jugador debe esquivar los enemigos y durar la mayor cantidad de tiempo 
* los enemigos se generar en diferentes posciciones cada vez que desaparecen de la pantalla
* al colicionar con el auto se genera un sprite de explosion y se restan 50 puntos a la barra de vida
* a medida que pasa el tiempo el score se incrementa, este es almacenado en la base de datos y mostrado de mayor a menor
  
![turbo revolution 22_7_2023 19_13_44 (2)](https://github.com/bautista-escalante/turbo-revolution/assets/123372673/5fd74729-9230-4689-a76b-4f40e8e77113)

# pestañas 

### inicio 
aca el usuario puede ver la pantalla de carga y presionar enter para iniciar
![menu principal 23_7_2023 13_24_30](https://github.com/bautista-escalante/turbo-revolution/assets/123372673/40e9405a-4dcc-42bf-9ea7-9bf7a8e93380)

```python
import pygame 
from constantes import *

pygame.init() 
imagen=pygame.image.load("C:\\programacion I\\turbo revolution\\menu\\menu.png") 
imagen= pygame.transform.scale(imagen,(ALTO_VENTANA,ANCHO_VENTANA))

pantalla=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA)) 
pygame.display.set_caption("menu principal") 

bandera=True
while bandera:  
    pantalla.blit(imagen,(0,0))
    lista = pygame.event.get() 
    for evento in lista:
        if evento.type == pygame.QUIT:
            bandera= False
        elif evento.type == pygame.KEYDOWN :
            if evento.key == pygame.K_RETURN:
                import pedir_dato 
    pygame.display.flip()
pygame.quit()
```

### pedir nombre
aca el usuario debe ingresar su nombre antes de empezar a jugar, este es guardado en la base de datos
```python
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

imagen=pygame.image.load("C:\\programacion I\\turbo revolution\\menu\\nombre.png") 
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
```














