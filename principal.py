import pygame 
import colores 
#from objetos import Obstaculo 
import random
import sqlite3 
import funciones

#### "constantes" ###   
ALTO=700 
ANCHO=500 
TAMAÑO_AUTO=(80,80)
posicion_auto=[200,550] 
linea1=[255,0,5,ALTO] 
linea2=[245,0,5,ALTO] 
FPS=60 

pygame.init()  
#pygame.mixer.init()
auto1= pygame.image.load("imagen\\auto.png") 
auto1= pygame.transform.scale(auto1,TAMAÑO_AUTO)
#### texto #### 
fuente= pygame.font.SysFont("arias",40) 
#### objetos #### 
#auto2=Obstaculo(TAMAÑO_AUTO,ANCHO,ALTO,3,5 ) 
##### cantidad de vidas #### 
cantidad_vidas=funciones.crear_lista(3) 
### rect ###  
rect1= auto1.get_rect() 
#### tiempo ####
timer = pygame.USEREVENT 
pygame.time.set_timer(timer,10) 
reloj = pygame.time.Clock()
### aleatorio ###
num_ramdom=random.randint(0,2)

pantalla= pygame.display.set_mode((ANCHO,ALTO))   
pygame.display.set_caption("turbo revolution")  
#### sound track ####  
pygame.mixer.music.load("audios\soundtrack.mp3") 
pygame.mixer.music.play(-1) 
pygame.mixer.music.set_volume(0.4) 

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
        score=100 
        pantalla.blit(auto1,posicion_auto) 
        #### coliciones ####

        vidas=funciones.actualizar_pantalla(cantidad_vidas,False,pantalla)
        if cantidad_vidas[0]["vidas"] == 0 and cantidad_vidas[1]["vidas"] == 0 and cantidad_vidas[2]["vidas"] == 0: 
            #### game over ####
            with sqlite3.connect("data.db") as conexion:
                #### insertar datos #####
                    conexion.execute("UPDATE jugador SET score = ?",(score,)) 
            try:
                    conexion.commit()
            except Exception:
                    print("Error") 
            cantidad_vidas=funciones.crear_lista(3) 
            import gameover  
        pygame.display.update()
        pygame.display.flip()
pygame.quit() 
""" auto2.actializar(pantalla,3) 
        print(auto2.posicion[1])
        if auto2.posicion[1]>ALTO: 
auto2.posicion[0]=random.randrange(0, ANCHO -TAMAÑO_AUTO[1] ,200) """
        
        #enemigos=auto2.crear_lista(num_ramdom) 
        #for obstaculos in enemigos:
        #### coliciones #####

