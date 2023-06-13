import pygame
import random

class Obstaculo:
    def __init__(self,tamaño:tuple,ancho:int,alto:int,velocidad:int): 
        self.tamaño=tamaño 
        self.ancho=ancho 
        self.alto=alto
        self.posicion= self.crear_posicion()  
        self.velocidad=self.crear_movimiento(velocidad) 

    def crear_posicion(self)->list: 
        x= random.randrange(0, self.ancho - self.tamaño[0],200) 
        return [x,0]

    def crear_movimiento(self,velocidad)->list: 
        self.posicion[1]=self.posicion[1]+ velocidad
        return self.posicion      

    def dic_obstaculos(self,cantidad:int,tipo:int):
        if tipo==1:
            imagen= pygame.image.load("imagen\\auto2.png" )
            imagen = pygame.transform.scale(imagen, (80,80))
        elif tipo==2:
            imagen= pygame.image.load("imagen\\auto3.png" )
            imagen = pygame.transform.scale(imagen, (80,80))
        elif tipo==3:
            imagen= pygame.image.load("imagen\\muro.png" )
            imagen = pygame.transform.scale(imagen, (100,80))
        elif tipo==4:
            imagen= pygame.image.load("imagen\\mancha.png" )
            imagen = pygame.transform.scale(imagen, (40,40))
        diccionario = {}
        for i in range(cantidad):
            diccionario["imagen"] =imagen 
            diccionario["rect"] = imagen.get_rect()
        return diccionario 
    
    def crear_lista(self,num1,num2):
        lista=[]
        for i in self.dic_obstaculos(num1,num2):
            lista.append(i)
        return lista
    
    def actualizar_pantalla(self,lista:list,rect_auto)->bool:
        for i in lista:
            if  rect_auto.colliderect(i["rect"]):
                return True
            else:
                return False

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


class vida:
    def __init__(self,imagen,posicion,cantidad_vidas) -> None:
        self.imagen=imagen
        self.posicion=posicion
        self.vidas=cantidad_vidas 

    def asignar_vida(self)->dict:
        imagen = pygame.image.load(self.imagen)
        imagen = pygame.transform.scale(imagen,(self.posicion))
        dic_vida = {}
        dic_vida["imagen"] = imagen
        dic_vida["visible"] = True
        return dic_vida

    def crear_lista(self,cantidad)->list:
        lista_vidas = []
        for i in range(cantidad):
            lista_vidas.append(self.asignar_vida())
        return lista_vidas

    def actualizar_pantalla(self,lista,colicion:bool, pantalla)->None: 
        for vida in lista: 
            if colicion==True:
                vida["visible"] = False
            elif colicion==False and vida["visible"] == True:
                pantalla.blit(vida["imagen"],(0,30))





