import pygame

pygame.init()

# Pygame 
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 6
FPS = 120
GREY = (29, 29, 29)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand")

clock = pygame.time.Clock()
# simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

#