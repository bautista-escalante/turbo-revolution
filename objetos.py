from typing import Any
import pygame
import random
import colores 
from tkinter import * 

class Obstaculo:
    def __init__(self,tamaño:tuple,ancho:int,alto:int,velocidad:int,imagen): 
        self.tamaño=tamaño 
        self.imagen=imagen
        self.ancho=ancho 
        self.alto=alto
        self.posicion= self.crear_posicion()  
        self.velocidad=self.crear_movimiento(velocidad) 

    def crear_posicion(self)->list: 
        x= random.randrange(0, self.ancho - self.tamaño[0],200) 
        return [x,0]

    def crear_movimiento(self,velocidad): 
        self.posicion[1]=self.posicion[1]+ velocidad
        return self.posicion  
        
    def crear_imagen(self, imagen):
        imagen = pygame.image.load(self.imagen)
        imagen = pygame.transform.scale(imagen, self.tamaño)
        return imagen  
         
    def crear_rect(self):
        rect=self.crear_imagen(self.imagen)
        rect=rect.get_rect()
        return rect 

    def colicionar(self,auto)->bool: 
        rect=self.crear_rect()
        if rect.colliderect(auto):
            return True
        else:
            return False     

### crear lista de obstaculos ###

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



