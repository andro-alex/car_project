import pygame
from constants import CAR_SPEED, BLINK_SPEED
from resources import *



class Car():
    def __init__(self, speed):
        self.speed = speed

    def acceleration():
        pass


class TurnSignal():
    def __init__(self, car_signals, position, signal_index, toggle_key):
        self.signals = car_signals
        self.position = position
        self.signal_index = signal_index
        self.toggle_key = toggle_key
        self.state = "off"
        self.frame = 0
        self.blink_counter = 0
        self.previous_key = False
        self.other = None # Link to the other turn signal for mutual exclusivity

    def turn_on(self):
        self.state = "on"
        self.frame = 0
        self.blink_counter = 0
        if self.other and self.other.state == "on": # Cancel the other signal if it's on
            self.other.turn_off()   

    def turn_off(self):
        self.state = "off"
        self.frame = 0
        self.blink_counter = 0
        self.previous_key = False

    def turn_signal_toggle(self):
        if self.state == "off":
            self.turn_on()
        else:
            self.turn_off()

    def update(self):
        if getattr(self, 'locked', False):
            return  # Skip update if locked (used for hazard signal to prevent toggling)    
        
        keys = pygame.key.get_pressed()

        if keys[self.toggle_key] and not self.previous_key:
            self.turn_signal_toggle() #Only toggle when the key is pressed, not held down (On the FIRST frame)

        self.previous_key = keys[self.toggle_key]

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

class HazardSignal(TurnSignal):
    def __init__(self, car_signals, hazard_images, position, left_signal, right_signal, toggle_key):
        super().__init__(car_signals, position, 0, toggle_key)
        self.hazard_signal = hazard_images
        self.left_signal = left_signal
        self.right_signal = right_signal
        self.state = "off" # Start with hazard off

    def turn_on(self):
        self.state = "on"
        self.frame = 0
        self.blink_counter = 0
        self.left_signal.state = "on"
        self.right_signal.state = "on" # Turn on both signals when hazard is activated  
        self.left_signal.locked = True # Lock the left signal to prevent toggling while hazard is on
        self.right_signal.locked = True # Lock the right signal to prevent toggling while hazard is on

    def turn_off(self):
        super().turn_off()
        self.left_signal.turn_off()
        self.right_signal.turn_off() # Turn off both signals when hazard is deactivated 
        self.left_signal.locked = False # Unlock the left signal to allow toggling while hazard is off
        self.right_signal.locked = False # Unlock the right signal to allow toggling while hazard is off

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[self.toggle_key] and not self.previous_key:
            self.turn_signal_toggle() #Only toggle when the key is pressed, not held down (On the FIRST frame)

        self.previous_key = keys[self.toggle_key]

        if self.state == "on":
            self.blink_counter += 1
            if self.blink_counter >= BLINK_SPEED:
                self.frame = 1 - self.frame
                self.blink_counter = 0
                # Sync the left and right signals with the hazard blinking
                self.left_signal.frame = self.frame
                self.right_signal.frame = self.frame

    def draw(self, screen):
        if self.state == "on":
            image = self.hazard_signal["on"]
        else:
            image = self.hazard_signal["off"]

        screen.blit(image, self.position)
