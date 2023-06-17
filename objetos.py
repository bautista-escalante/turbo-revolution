import pygame
import random 
 
class Obstaculo:
    def __init__(self,tamaño:tuple,ancho:int,alto:int,velocidad:int,cantidad): 
        self.tamaño=tamaño 
        self.ancho=ancho 
        self.alto=alto 
        self.posicion= self.crear_posicion()  
        self.velocidad=self.crear_movimiento(velocidad,self.crear_lista(cantidad)) 

    def crear_posicion(self)->list: 
        x= random.randrange(0, self.ancho - self.tamaño[0],200) 
        return [x,0] 

    def crear_movimiento(self,velocidad,lista)->list:  
        for rect in lista: 
           rect["rect"].y += velocidad  
        self.posicion[1] = self.posicion[1]+1 

    def dic_obstaculos(self,cantidad):
        imagen= pygame.image.load("imagen\\auto2.png" ) 
        imagen = pygame.transform.scale(imagen, (80,80)) 
        diccionario = {}
        for i in range(cantidad): 
            diccionario["imagen"] =imagen 
            diccionario["rect"] = imagen.get_rect()
            diccionario["posicion"]=self.crear_posicion()
        return diccionario    

    def crear_lista(self,cantidad):
        lista=[] 
        lista.append(self.dic_obstaculos(cantidad)) 
        return lista 
    
    def actializar(self,pantalla,cantidad):
        movimiento=self.crear_movimiento(self.velocidad,self.velocidad) 
        lista=self.crear_lista(cantidad)
        for i in lista: 
            pantalla.blit(i["imagen"],i["rect"])
            self.crear_movimiento(3)


""" def colicionar(self,lista:list,rect_auto)->bool:
        for i in lista:
            if  rect_auto.colliderect(i["rect"]):
                return True
            else:
                return False"""

class sprite(pygame.sprite.Sprite) :
    def __init__(self,imagen,alto):
        super().__init__()
        self.imagen = pygame.image.load(imagen)
        self.imagen.set_clip(pygame.Rect(0,0,40,40))
        self.imagen = self.imagen.subsurface( self.imagen.set_clip())
        self.rect = self.imagen.get_rect()
        self.marco = 0
        self.estado = {0:{0,40,52,76},1:{40,40,52,76},2:{80,40,52,76},3:{80,40,52,76},4:{80,80,52,76},5:{80,120,52,76}}

    def get_frame(self,frame_set):
        self.marco +=1
        if self.marco> (len(frame_set)):
            self.marco=0
        return frame_set[self.marco]

    def update(self) -> None:
        self.rect.y +=10
        if self.rect> self.alto:
            self.rect.botton=0




