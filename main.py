import pygame
import sys
from constants import *
from car import *
from resources import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    title = pygame.display.set_caption("Awesome Car")
    clock = pygame.time.Clock()
    dt = 0
    left_signal = TurnSignal(car_signals, (LEFT_X, SIGNAL_Y), 0, pygame.K_q)
    right_signal = TurnSignal(car_signals, (RIGHT_X, SIGNAL_Y), 1, pygame.K_e)
    left_signal.other = right_signal # Link the left signal to the right signal for mutual exclusivity  
    right_signal.other = left_signal # Link the right signal to the left signal for mutual exclusivity
    hazard_signal = HazardSignal(car_signals, hazard_images, (HAZARD_X, HAZARD_Y), left_signal, right_signal, pygame.K_h) # Hazard signal using the same class for simplicity
   
    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        
        screen.fill("black")
        hazard_signal.update()
        left_signal.draw(screen)
        right_signal.draw(screen)
        left_signal.update()
        right_signal.update()
        hazard_signal.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

main()
