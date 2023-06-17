import pygame

ANCHO_VENTANA=600
ALTO_VENTANA=600 

pygame.init()
imagen=pygame.image.load("menu\\game over.png") 
imagen= pygame.transform.scale(imagen,(ALTO_VENTANA,ANCHO_VENTANA))

pantalla=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("menu principal")

bandera=True
while bandera: 
    pantalla.blit(imagen,(0,0))
    lista = pygame.event.get()
    for evento in lista:
        if evento.type == pygame.QUIT:
            bandera= False
        elif evento.type == pygame.KEYDOWN :
            if evento.key == pygame.K_RETURN:
                import menu 
            elif evento.key == pygame.K_SPACE:
                import score    
    
    pygame.display.flip()
pygame.quit()