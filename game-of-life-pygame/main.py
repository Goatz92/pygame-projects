import pygame, sys
from simulation import Simulation
from fps import FPS_display

pygame.init()

# Static vars

BLACK = (255, 255, 255)
GREY = (29, 29, 29)
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
CELL_SIZE = 12
FPS = 12

# Set window resolution in pygame
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Window Title
pygame.display.set_caption("Game of Life")

# time.Clock() method tracks an amount of time
# In this instance it is used to control the game's fps
clock = pygame.time.Clock()

simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
font = pygame.font.SysFont("Arial" , 18 , bold = True)


def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    window.blit(fps_t,(0,0))

# Main Loop
while True:
    
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // CELL_SIZE
            column = pos[0] // CELL_SIZE
            simulation.toggle_cell(row, column)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.start()
                pygame.display.set_caption("Game of Life is Running")
            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("Game of life has stopped")
            elif event.key == pygame.K_f:
                FPS += 2
            elif event.key == pygame.K_s:
                if FPS > 5:
                    FPS -= 2
            elif event.key == pygame.K_r:
                simulation.create_random_state()
            elif event.key == pygame.K_c:
                simulation.clear()
                
    # 2. Update State
    simulation.update()

    # 3. Draw
    window.fill(GREY)
    simulation.draw(window)

    pygame.display.update()
    print(clock.get_fps())
    clock.tick(FPS)
    FPS_display()


