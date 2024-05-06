# Class representing the implemented microcontroller.
# Initially this will be a wrapper for the Pi Pico W
from machine import Pin

class Controller:
    #class variables
    pins = []
    #class functions
    def __init__(self, graphics_driver, pins):
        _pins = pins
        return
    
    def send(self, data):
        data = (9 << 12) | (data << 2)
        return