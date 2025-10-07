import pygame
import sys
from clock import AnalogClock

pygame.init()

# Resolution
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Window Colours
LIGHT_BLUE = (204, 255, 229)

# Functional Variables
is_running = True

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Analog Clock")

clock = pygame.time.Clock()
analog_clock = AnalogClock(250, (300, 300), WINDOW_WIDTH, WINDOW_HEIGHT)


# Main Loop
while is_running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Update State
    analog_clock.update()

    # 3. Draw
    window.fill(LIGHT_BLUE)
    analog_clock.draw(window)

    pygame.display.update()
    clock.tick(15)