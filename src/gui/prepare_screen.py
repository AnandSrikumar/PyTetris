import pygame
from ..calculations.dims import *
import random

class GameScreen:
    def __init__(self, screen, constants, event_state):
        self.screen = screen
        display_info = pygame.display.Info()
        self.screen_width = display_info.current_w
        self.screen_height = display_info.current_h
        self.constants = constants
        self.inititialized = False
        self.event_state = event_state

    def draw_game_container(self, color):
        cont_width, cont_height = self.screen_width-50, self.screen_height
        dimensions = place_item_at_screen_center(self.screen_width,
                                           self.screen_height,
                                           cont_width, cont_height)
        self.grid_start_x = dimensions[0]
        self.grid_start_y = dimensions[1]
        self.container_width = dimensions[2]
        self.container_height = dimensions[3]
        self.event_state.set_container_coords(self.grid_start_x, 
                                              self.grid_start_y,
                                              self.container_width,
                                              self.container_height)

        pygame.draw.rect(self.screen, color, dimensions)

    def draw_boundaries(self):
        random_colors = self.constants['RANDOM_COLORS']
        boundaries \
            = calculate_boundaries_container(self.grid_start_x,
                                             self.grid_start_y,
                                             self.container_width,
                                             self.container_height)
        cidx = 0
        for x in boundaries:
            boundary = x['boundary']
            line_width = x['width']
            color_random = random_colors[cidx]
            cidx += 1
            pygame.draw.rect(self.screen, color_random, boundary, width=line_width)
            if cidx >= len(random_colors):
                cidx = 0
        
        


    # def draw_grid_container(self, color):
    #     block_size = self.constants['BLOCK_SIZE']
    #     grid_rows, grid_cols = self.constants['GRID_BLOCKS']
    #     dimensions = calculate_grid_dims(self.grid_start_x,
    #                                      self.grid_start_y,
    #                                      self.container_width,
    #                                      self.container_height,
    #                                      block_size,
    #                                      grid_rows,
    #                                      grid_cols)
    #     pygame.draw.rect(self.screen, color, dimensions)
