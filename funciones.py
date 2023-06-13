import pygame

pygame.init()

# Obtener la lista de fuentes disponibles
font_names = pygame.font.get_fonts()

# Imprimir la lista de fuentes
for font_name in font_names:
    print(font_name)