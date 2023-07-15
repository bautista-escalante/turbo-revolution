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




