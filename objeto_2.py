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