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
            lista.append(self.crear_obstaculo((random.randrange(0,self.ancho)+i*100,0)))
        return lista

    def actualizar(self, lista, pantalla, velocidad):
        for i in lista:
            i["rect"].y += velocidad
            if i["rect"].y > pantalla.get_height():
                # Si el obstáculo sale de la pantalla, se reinicia en la posición inicial
                i["rect"].y = 0
                i["rect"].x = random.randint(0,self.ancho)
            pantalla.blit(i["imagen"], i["rect"])
        return lista

    def colicionar(self,lista,rect,pantalla,)->bool:
        for i in lista: 
            colicion=rect.colliderect(i["rect"])
            personaje_rect=pygame.Rect(i["rect"])
            pygame.draw.rect(pantalla, (0,0,0,128), personaje_rect)
            if colicion:
                i["rect"].y=1000
        return colicion


class Moneda(pygame.sprite.Sprite):
    def __init__(self,tamaño:list,imagen ) -> None: 
        super().__init__() 
        self.tamaño=tamaño 
        self.image = pygame.image.load(imagen).convert() 
        self.image.set_colorkey(colores.BLACK) 
        self.rect = self.image.get_rect() 

    def update(self, ) -> None:
        self.rect.y +=10
        if self.rect.top>self.tamaño[1]: 
            self.rect.bottom =0
    
    def cantidad(self,cantidad): 
        for i in range(cantidad):
            meteor = Moneda()
            meteor.rect.x = random.randrange(900)
            meteor.rect.y = random.randrange(600)
