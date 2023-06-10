import pygame 
import colores 
from objetos import Obstaculo 
import random
import sqlite3

#### "constantes" ###   
ALTO=700 
ANCHO=500 
TAMAÑO_AUTO=(80,80)
posicion_auto=[200,550] 
linea1=[255,0,5,ALTO] 
linea2=[245,0,5,ALTO] 
cantidad_vidas =3 
FPS=120
minutos=00

imagen2="imagen\\auto2.png" 
imagen3="imagen\\auto3.png" 
imagen_muro="imagen\\muro.png" 
imagen_mancha ="imagen\\mancha.png"

pygame.init() 
pygame.mixer.init()
auto1= pygame.image.load("imagen\\auto.png") 
auto1= pygame.transform.scale(auto1,TAMAÑO_AUTO)
#### texto ####
fuente= pygame.font.SysFont("arias",40)
#### objetos #### 
auto2=Obstaculo(TAMAÑO_AUTO,ANCHO,ALTO,3,imagen2 ) 
auto3=Obstaculo(TAMAÑO_AUTO,ANCHO,ALTO,5,imagen3)  
muro=Obstaculo((100,70),ANCHO,ALTO,3,imagen_muro) 
mancha=Obstaculo((40,40),ANCHO,ALTO,3,imagen_mancha) 
#### posiciones iniciales####  
posicion2=auto2.crear_posicion() 
posicion3=auto3.crear_posicion() 
posicion4=muro.crear_posicion()  
posicion5=mancha.crear_posicion()
#### imagenes #### 
imagen_auto2=auto2.crear_imagen(imagen2) 
imagen_auto3=auto3.crear_imagen(imagen3) 
imagen_muro=muro.crear_imagen(imagen_muro)
imagen_mancha=mancha.crear_imagen(imagen_muro)
### rect ###  
rect1= auto1.get_rect()
rect2= auto2.crear_rect()
rect3= auto3.crear_rect()
rect4=muro.crear_rect() 
#### tiempo ####
timer = pygame.USEREVENT 
pygame.time.set_timer(timer,10) 
reloj = pygame.time.Clock()

pantalla= pygame.display.set_mode((ANCHO,ALTO))   
pygame.display.set_caption("turbo revolution")  
#### sound track ####  
pygame.mixer.music.load("audios\\soundtrack.mp3") 
pygame.mixer.music.play(-1) 
pygame.mixer.music.set_volume(0.2)

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
        pantalla.blit(imagen_auto2,velocidad)  
        pantalla.blit(imagen_auto3,velocidad3)  
        pantalla.blit(imagen_muro,velocidad4) 
        pantalla.blit(imagen_mancha,velocidad5) 
        cantidad_vidas -= 1
        if cantidad_vidas == 0: 
            with sqlite3.connect("data.db") as conexion:
                #### insertar datos #####
                    conexion.execute("insert into jugador(name,time,score)"
                    "values (?,?,?)", ("?", 0,0)) 
            try:
                    conexion.commit()# Actualiza los datos realmente en la tabla
            except Exception:
                    print("Error") 
            try:
                    #### imprimir en pantalla ####
                    cursor=conexion.execute("SELECT * FROM jugador")
                    for fila in cursor:
                        print(fila) 
            except Exception:
                    print("Error") 
            cantidad_vidas= 3 
            import gameover 
            print("game over")
        pygame.display.update()
        pygame.display.flip()
pygame.quit() 



