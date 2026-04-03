import pygame
import sys
from constants import *
from car import *
from resources import car_signals

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    title = pygame.display.set_caption("Awesome Car")
    clock = pygame.time.Clock()
    dt = 0
    left_signal = LeftSignal(car_signals, (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2.5)) 
    right_signal = RightSignal(car_signals, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.5))

    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        screen.fill("black")
        left_signal.draw(screen)
        right_signal.draw(screen)
        left_signal.update()
        right_signal.update()


        pygame.display.flip()

        dt = clock.tick(60) / 1000

main()
