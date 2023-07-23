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

![menu principal 23_7_2023 14_52_02](https://github.com/bautista-escalante/turbo-revolution/assets/123372673/e0e8a1de-1206-453d-b674-ea6e2aa5a02e)

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
# objetos
### sprite de explosion
este objeto necesita una lista con las imagenes y tiene el metodo animar() que ejecuta la secuencia de imagenes 
```python
import pygame

class Explosion():
    def __init__(self, tamaño: list, lista_animacion) -> None:
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.contador_pasos = 0
        self.lista = self.crear_lista(lista_animacion)

    def crear_lista(self, lista) -> list:
        nueva_lista = []
        for imagen in lista:
            dic = {}
            imagen = pygame.transform.scale(imagen, (self.ancho, self.alto))
            dic["imagen"] = imagen
            nueva_lista.append(dic)
        return nueva_lista 

    def animar(self, pantalla, posicion):
        if self.contador_pasos >= len(self.lista):
            self.contador_pasos = 0
        pantalla.blit(self.lista[self.contador_pasos]["imagen"], posicion)
        self.contador_pasos += 1

lista_animacion=[pygame.image.load(explosion1),
                 pygame.image.load(explosion2),
                 pygame.image.load(explosion3),
                 pygame.image.load(explosion4),]
sprite=Explosion([70,70],lista_animacion)
```
### obstaculo
este objeto crea la cantidad de enemigos, la posicion, la velocidad  a la que desplazan y verifica la colicion
```python
import pygame
import random
import colores

class Obstaculo:
    def __init__(self, tamaño: tuple, ancho: int, alto: int,imagen):
        self.tamaño=tamaño
        self.ancho=ancho
        self.alto=alto
        self.imagen=imagen

    def crear_obstaculo(self,posicion:tuple)->dict:
        rect = self.imagen.get_rect()
        rect.x=posicion[0]
        rect.y=posicion[1]
        dic = {}
        dic["imagen"] = self.imagen
        dic["rect"] = rect
        return dic
    
    def crear_lista(self,cantidad):
        lista=[]
        for i in range(cantidad):
            lista.append(self.crear_obstaculo((random.randrange(0,self.ancho)+i*300,0)))
        return lista

    def actualizar(self, lista, pantalla, velocidad):
        for i in lista:
            i["rect"].y += velocidad
            if i["rect"].y > self.alto:
                # Si el obstáculo sale de la pantalla, se reinicia en la posición inicial
                i["rect"].y = 0
                i["rect"].x = random.randint(0,self.ancho)
            pantalla.blit(i["imagen"], i["rect"])
        return lista

    def colicionar(self,lista,rect,pantalla,)->bool:
        for i in lista: 
            colicion=rect.colliderect(i["rect"])
            personaje_rect=pygame.Rect(i["rect"])
            pygame.draw.rect(pantalla, colores.BLACK, personaje_rect)
            if colicion:
                i["rect"].y=1000
        return colicion
auto2=Obstaculo(TAMAÑO_AUTO,ANCHO,ALTO,imagen )
lista_enemigos=auto2.crear_lista(4)
colicion=auto2.colicionar(lista_enemigos,rect1,pantalla)
auto2.actualizar(lista_enemigos,pantalla,3)
```
# principal
### iniciacion e instancias
aca se importan todos los modulos, se intstancian objetos anteriores, se inicializa pygame, se configura la musica, etc.
```python
import pygame 
import colores 
from constantes import *
from objeto_1 import Obstaculo 
from objeto_2 import Explosion
import sqlite3 
import os 

pygame.init()  
pygame.mixer.init()

lista_animacion=[pygame.image.load(explosion1),
                 pygame.image.load(explosion2),
                 pygame.image.load(explosion3),
                 pygame.image.load(explosion4),]
auto1= pygame.image.load("C:\\programacion I\\turbo revolution\\imagen\\auto.png") 
auto1= pygame.transform.scale(auto1,TAMAÑO_AUTO)
imagen=pygame.image.load("C:\\programacion I\\turbo revolution\\imagen\\auto3.png")
imagen= pygame.transform.scale(imagen,TAMAÑO_AUTO)
#### texto #### 
ruta_fuente = os.path.join('C:\\programacion I\\turbo revolution\\mega pixel','C:\\programacion I\\turbo revolution\\mega pixel\\00TT.TTF')
fuente = pygame.font.Font(ruta_fuente, 30)
#### objetos #### 
auto2=Obstaculo(TAMAÑO_AUTO,ANCHO,ALTO,imagen ) 
sprite=Explosion([70,70],lista_animacion)
##### cantidad de enemigos #### 
barra_vida=300 
lista_enemigos=auto2.crear_lista(4)
#### tiempo ####
timer = pygame.USEREVENT 
pygame.time.set_timer(timer,10) 
reloj = pygame.time.Clock()

pantalla= pygame.display.set_mode((ANCHO,ALTO))   
pygame.display.set_caption("turbo revolution")   
#### sound track ####  
pygame.mixer.music.load("C:\\programacion I\\turbo revolution\\audios\\soundtrack.mp3") 
pygame.mixer.music.play(-1) 
pygame.mixer.music.set_volume(0.4) 
```
### bucle
aca se deterctan los eventos del teclado, se verifca la colicion se verifica la barra de vida, se incremeta el score en base al tiempo, etc.
```python
menu=True 
while menu:
    reloj.tick(FPS)
    tiempo_actual = pygame.time.get_ticks()
    score=round(tiempo_actual/1000)
    lista = pygame.event.get() 
    for evento in lista:
        if evento.type== pygame.QUIT: 
            menu= False  
        if evento.type==pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT: 
                posicion_auto[0]= posicion_auto[0] +100 
            if evento.key == pygame.K_LEFT: 
                posicion_auto[0]= posicion_auto[0] -100   
        if evento.type== pygame.USEREVENT: 
             #### bordes #### 
            if evento.type==timer and posicion_auto[0]<0: 
                    posicion_auto[0]= 0 
            elif evento.type==timer and posicion_auto[0]>ANCHO: 
                    posicion_auto[0]= ANCHO - TAMAÑO_AUTO[1] 

         #### fondo #### 
        pantalla.fill(colores.BLACK) 
        pygame.draw.rect(pantalla,colores.YELLOW3,linea1) 
        pygame.draw.rect(pantalla,colores.YELLOW3,linea2) 
        #### score ####
        texto= "score: "+str(score)
        dato = fuente.render(texto, True, colores.YELLOW1)
        pantalla.blit(dato,(40,40)) 
        ### rect ###  
        rect1= pygame.Rect(posicion_auto,TAMAÑO_AUTO)
        personaje_rect=pygame.Rect(rect1)
        pygame.draw.rect(pantalla, colores.BLACK, personaje_rect)
        pantalla.blit(auto1,posicion_auto)
        #### coliciones #### 
        colicion=auto2.colicionar(lista_enemigos,rect1,pantalla)
        auto2.actualizar(lista_enemigos,pantalla,3)
        #### barra de vida ####
        pygame.draw.rect(pantalla, colores.GREEN1, (10,10, barra_vida, 20))
        if colicion:
            sprite.animar(pantalla,posicion_auto)
            barra_vida -=50
        if barra_vida==0: 
            #### game over #### 
            with sqlite3.connect("data.db") as conexion: 
                cursor = conexion.execute("SELECT name FROM jugador")
                datos = cursor.fetchall()
                for  fila in datos:
                    nombre="{0}".format(fila[0])
                #### insertar datos #####
                conexion.execute("INSERT INTO jugador (name, score) VALUES (?, ?)",(nombre,score)) 
            try:
                    conexion.commit()
            except Exception:
                    print("Error") 
            import gameover  
        pygame.display.update()
        pygame.display.flip()
pygame.quit() 
```
### game over 
al perder se guarda el score en la base de datos y se dirige a el modulo gameover
al usuario se le permite volver a jugar o ver su score comparado con el resto

![game over 23_7_2023 15_35_35](https://github.com/bautista-escalante/turbo-revolution/assets/123372673/b43639a7-6d1b-4df6-bd7c-4bc369f95834)

``` python
import pygame 
from constantes import *

pygame.init()
imagen=pygame.image.load("C:\\programacion I\\turbo revolution\\menu\\game over.png") 
imagen= pygame.transform.scale(imagen,(ALTO_VENTANA,ANCHO_VENTANA))

pantalla=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("game over")

bandera=True
while bandera: 
    pantalla.blit(imagen,(0,0))
    lista = pygame.event.get()
    for evento in lista:
        if evento.type == pygame.QUIT:
            bandera= False
        elif evento.type == pygame.KEYDOWN :
            if evento.key == pygame.K_RETURN:
                import menu 
            elif evento.key == pygame.K_SPACE:
                import score    
    
    pygame.display.flip()
pygame.quit()
```
### score
los scores de los mejores 5 jugadores

![menu principal 23_7_2023 15_38_48](https://github.com/bautista-escalante/turbo-revolution/assets/123372673/dadd6c55-3247-460b-b95a-e02766be1c2e)

```python
import pygame
import os
import colores
import sqlite3 
from constantes import *

ANCHO_VENTANA=600
ALTO_VENTANA=600 

pygame.init()
imagen=pygame.image.load("C:\\programacion I\\turbo revolution\menu\\score.png") 
imagen= pygame.transform.scale(imagen,(ALTO_VENTANA,ANCHO_VENTANA)) 

pantalla=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA)) 
pygame.display.set_caption("menu principal") 

ruta_fuente = os.path.join('C:\\programacion I\\turbo revolution\\mega pixel', 'C:\\programacion I\\turbo revolution\\mega pixel\\00TT.TTF')
fuente = pygame.font.Font(ruta_fuente, 30)

texto = fuente.render("press enter to return to the menu", True, colores.YELLOW1)  
dato = fuente.render("nombres  puntajes", True, colores.YELLOW1)  

with sqlite3.connect("data.db") as conexion: 
    try: 
        #### imprimir en pantalla #### 
        cursor=conexion.execute("SELECT * FROM jugador") 
        datos = cursor.fetchall()
        
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

```









