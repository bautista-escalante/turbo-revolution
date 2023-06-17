import pygame

def asignar_vida(cantidad:int)->dict: 
    imagen = pygame.image.load("imagen\\corazon.png")
    imagen = pygame.transform.scale(imagen,(30,30))
    dic_vida = {}
    dic_vida["imagen"] = imagen
    dic_vida["visible"] = True 
    dic_vida["vidas"] = cantidad
    return dic_vida  

def crear_lista(cantidad)->list:
    lista_vidas = []
    for i in range(cantidad):
        lista_vidas.append(asignar_vida(cantidad))
    return lista_vidas 

def actualizar_pantalla(lista,colicion:bool, pantalla)->None: 
    x=20
    for vida in lista: 
        if colicion==True:
            vida["vidas"] -=1
            vida["visible"] = False
        elif colicion==False and vida["visible"] == True:
            pantalla.blit(vida["imagen"],(x,0))
            x +=30
 










