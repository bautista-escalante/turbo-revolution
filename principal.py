import pygame 
import colores 
from objetos import Obstaculo 
from objetos import Explosion
import sqlite3

#### "constantes" ###   
ALTO=700 
ANCHO=500 
TAMAÑO_AUTO=(80,80)
posicion_auto=[200,550] 
linea1=(255,0,5,ALTO)
linea2=(245,0,5,ALTO)
FPS=60
score=0

pygame.init()  
pygame.mixer.init()

lista_animacion=[pygame.image.load("sprites\\explosion\\1.png"),
                 pygame.image.load("sprites\\explosion\\2.png"),
                 pygame.image.load("sprites\\explosion\\3.png"),
                 pygame.image.load("sprites\\explosion\\4.png"),]
auto1= pygame.image.load("imagen\\auto.png") 
auto1= pygame.transform.scale(auto1,TAMAÑO_AUTO)
imagen=pygame.image.load("imagen\\auto3.png")
imagen= pygame.transform.scale(imagen,TAMAÑO_AUTO)
#### texto #### 
fuente= pygame.font.SysFont("arias",40) 
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
pygame.mixer.music.load("audios\soundtrack.mp3") 
pygame.mixer.music.play(-1) 
pygame.mixer.music.set_volume(0.4) 
bandera=True
menu=True 
while menu:
    reloj.tick(FPS)
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
                #### insertar datos #####
                    conexion.execute("UPDATE jugador SET score = ?",(score,)) 
            try:
                    conexion.commit()
            except Exception:
                    print("Error") 
            import gameover  
        pygame.display.update()
        pygame.display.flip()
pygame.quit() 


