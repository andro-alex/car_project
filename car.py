import pygame
from constants import CAR_SPEED, BLINK_SPEED
from resources import *

class Car():
    def __init__(self, speed):
        self.speed = speed

    def acceleration():
        pass


class LeftSignal():
    def __init__(self, car_signals, position):
        self.signals = car_signals
        self.position = position
        self.state = "off"
        self.signal_index = 0  # 0 for left signal
        self.frame = 0  # 0 for off, 1 for on in flashing
        self.blink_counter = 0
        self.previous_q = False
   
    def turn_on(self):
        self.state = "on"
        self.frame = 0
        self.blink_counter = 0

    def turn_off(self):
        self.state = "off"
        self.frame = 0
        self.blink_counter = 0

    def turn_signal_toggle(self):
        if self.state == "off":
            self.turn_on()
        else:
            self.turn_off()

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q] and not self.previous_q:
            self.turn_signal_toggle()

        self.previous_q = keys[pygame.K_q]

        if self.state == "on":
            self.blink_counter += 1
            if self.blink_counter >= BLINK_SPEED:
                self.frame = 1 - self.frame
                self.blink_counter = 0

    def draw(self, screen):
        if self.state == "off":
            image = self.signals["off"][self.signal_index]
        else:
            state_key = "on" if self.frame == 1 else "off"
            image = self.signals[state_key][self.signal_index]
        screen.blit(image, self.position)

class RightSignal():
    def __init__(self, car_signals, position):
        self.signals = car_signals
        self.position = position
        self.state = "off"
        self.signal_index = 1  # 1 for right signal
        self.frame = 0  # 0 for off, 1 for on in flashing
        self.blink_counter = 0
        self.previous_e = False
        

    def turn_on(self):
        self.state = "on"
        self.frame = 0
        self.blink_counter = 0

    def turn_off(self):
        self.state = "off"
        self.frame = 0
        self.blink_counter = 0

    def turn_signal_toggle(self):
        if self.state == "off":
            self.turn_on()
        else:
            self.turn_off()

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_e] and not self.previous_e:
            self.turn_signal_toggle()

        self.previous_e = keys[pygame.K_e]

        if self.state == "on":
            self.blink_counter += 1
            if self.blink_counter >= BLINK_SPEED:
                self.frame = 1 - self.frame
                self.blink_counter = 0

    def draw(self, screen):
        if self.state == "off":
            image = self.signals["off"][self.signal_index]
        else:
            state_key = "on" if self.frame == 1 else "off"
            image = self.signals[state_key][self.signal_index]
        screen.blit(image, self.position)



