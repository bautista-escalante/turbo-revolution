import pygame 
import colores 
from objetos import Obstaculo 
from objetos import vida
import random
import sqlite3

#### "constantes" ###   
ALTO=700 
ANCHO=500 
TAMAÑO_AUTO=(80,80)
posicion_auto=[200,550] 
linea1=[255,0,5,ALTO] 
linea2=[245,0,5,ALTO] 
FPS=120
minutos=00

pygame.init() 
pygame.mixer.init()
auto1= pygame.image.load("imagen\\auto.png") 
auto1= pygame.transform.scale(auto1,TAMAÑO_AUTO)
#### texto ####
fuente= pygame.font.SysFont("arias",40)
#### objetos #### 
auto2=Obstaculo(TAMAÑO_AUTO,ANCHO,ALTO,3 ) 
auto3=Obstaculo(TAMAÑO_AUTO,ANCHO,ALTO,5)  
muro=Obstaculo((100,70),ANCHO,ALTO,3) 
mancha=Obstaculo((40,40),ANCHO,ALTO,3,) 
vidas=vida("imagen\\corazon.png",(20,30),3)
#### posiciones iniciales####  
posicion2=auto2.crear_posicion() 
posicion3=auto3.crear_posicion() 
posicion4=muro.crear_posicion()  
posicion5=mancha.crear_posicion()
##### cantidad de vidas ####
lista_vida = vidas.crear_lista(3) 
cantidad_vidas=3 
### rect ###  
rect1= auto1.get_rect()
#### tiempo ####
timer = pygame.USEREVENT 
pygame.time.set_timer(timer,10) 
reloj = pygame.time.Clock()
### aleatorio ###
num_ramdom=int(random.randint(0,2))
num_ramdom1=int(random.randint(0,4)) 

pantalla= pygame.display.set_mode((ANCHO,ALTO))   
pygame.display.set_caption("turbo revolution")  
#### sound track ####  
pygame.mixer.music.load("audios\\soundtrack.mp3") 
pygame.mixer.music.play(-1) 
pygame.mixer.music.set_volume(0.4) 

menu=True 
while menu:
    segundos= int(pygame.time.get_ticks()/1100)
    if segundos==60:
        minutos +=1 
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

        pantalla.blit(auto1,posicion_auto)  
        
        velocidad=auto2.crear_movimiento(2.4) 
        velocidad3=auto3.crear_movimiento(1.5) 
        velocidad4=muro.crear_movimiento(2.5) 
        velocidad5 = mancha.crear_movimiento(3.4)
        if velocidad[1]>ALTO and velocidad3[1]>ALTO and velocidad4[1]>ALTO and velocidad5[1]>ALTO: 
            velocidad[0]=random.randrange(0, ANCHO -TAMAÑO_AUTO[1] ,200) 
            velocidad3[0]=random.randrange(0, ANCHO -TAMAÑO_AUTO[1] ,200) 
            velocidad4[0]=random.randrange(0, ANCHO -150,200 ) 
            velocidad4[0]=random.randrange(0, ANCHO -40,200 ) 
            velocidad[1]=0 
            velocidad3[1]=0 
            velocidad4[1]=0 
            velocidad5[1]=0 
        score=0
        time=0
        enemigos=auto2.crear_lista(num_ramdom,num_ramdom1)
        for obstaculos in enemigos:
            pantalla.blit(obstaculos["imagen"],posicion2) 
        #### coliciones #####
        if auto2.actualizar_pantalla(enemigos,rect1) or auto3.actualizar_pantalla(enemigos,rect1) or muro.actualizar_pantalla(enemigos,rect1):
            cantidad_vidas -=1 
        elif mancha.actualizar_pantalla(enemigos,rect1): 
            pass
            #sprite 
        if cantidad_vidas == 0: 
            with sqlite3.connect("data.db") as conexion:
                #### insertar datos #####
                    conexion.execute("UPDATE jugador SET score = ?, time=?",(score,time)) 
            try:
                    conexion.commit()# Actualiza los datos realmente en la tabla
            except Exception:
                    print("Error") 
            cantidad_vidas= 3 
            import gameover 
            print("game over")
        pygame.display.update()
        pygame.display.flip()
pygame.quit() 
