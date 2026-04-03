import pygame
import os

#Car Turning Signals 

car_signals = {
    "off": [
        pygame.transform.smoothscale(pygame.image.load(os.path.join("resources", "img", "left_turn_signal_off.png")), (128, 128)),
        pygame.transform.smoothscale(pygame.image.load(os.path.join("resources", "img", "right_turn_signal_off.png")), (128, 128))
    ],

    "on": [
        pygame.transform.smoothscale(pygame.image.load(os.path.join("resources", "img", "left_turn_signal_on.png")), (128, 128)),
        pygame.transform.smoothscale(pygame.image.load(os.path.join("resources", "img", "right_turn_signal_on.png")), (128, 128))
    ]

}