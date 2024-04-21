import pygame
import sys
from ..calculations.shapes_movements import horizontal_movement, adjust_speeds

class EventHandle:
    def __init__(self, event_variables, gui_collisions, constants):
        self.events_mapper = {
            pygame.QUIT: self.quit_handler,
            pygame.KEYDOWN: self.keydown_handler,
            pygame.KEYUP: self.keyup_handler,
            pygame.MOUSEBUTTONDOWN: self.mousedown_handler,
            pygame.MOUSEBUTTONUP: self.mouseup_handler
        }
        self.event_variables = event_variables
        self.gui_collisions = gui_collisions
        self.constants = constants
        self.keys_pressed = {}

    def quit_handler(self, event):
        self.event_variables.set_running(False)
        sys.exit()

    def adjust_movement_speeds(self):
        pass

    def keydown_handler(self, event):
        if (event.key == pygame.K_q):
            self.event_variables.set_running(False)

        elif (event.key == pygame.K_DOWN):
            curr_movement_delay = self.event_variables.get_movement_delay()
            self.event_variables.set_movement_delay(60)

        elif(event.key == pygame.K_UP):
            curr_shape = self.event_variables.get_current_shape()
            curr_shape.current_rotation += 1
        
    def keyup_handler(self, event):
        if (event.key == pygame.K_DOWN):
            delay = adjust_speeds(self.event_variables, self.constants)
            self.event_variables.set_movement_delay(delay)

        if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            self.keys_pressed.pop(event.key, None)

    def mousedown_handler(self, event):
        self.event_variables.set_is_mouse_pressed(True)
        self.gui_collisions.mouse_down_collisions()
        

    def mouseup_handler(self, event):
        self.event_variables.set_is_mouse_pressed(False)


    def handle_event(self, event):
        type_func = self.events_mapper.get(event.type)
        if type_func:
            type_func(event)

        keys = pygame.key.get_pressed()
        self.event_variables.set_left_pressed(keys[pygame.K_LEFT])
        self.event_variables.set_right_pressed(keys[pygame.K_RIGHT])
