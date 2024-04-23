import pygame
from .event_states import *
from ..services.read_files import read_json
from ..game_entities.bag_of_seven import BagOfSeven
from ..game_entities.grid_matrix import GridMatrix

class StateLoader:
    def __init__(self, constants, event_state, screen):
        self.constants = constants
        self.event_state = event_state
        self.screen = screen
    
    def load_fonts(self):
        fonts = {'title':{}}
        states = self.event_state.get_all_event_states()
        for k, v in states.items():
            font_size = self.constants['TITLE_SIZES'][v]
            font_path = self.constants['TITLE_FONT']
            fnt = pygame.font.Font(font_path, font_size)
            fonts['title'][k] = fnt
        other_fonts = self.constants['menu_title_font']
        size, path = other_fonts['size'], other_fonts['path']
        other_fnt = pygame.font.Font(path, size)
        fonts['other_fonts'] = other_fnt

        text_font = other_fonts = self.constants['text_font']
        size, path = text_font['size'], text_font['path']
        text_fnt = pygame.font.Font(path, size)
        fonts['text_font'] = text_fnt

        self.fonts = fonts
        self.event_state.set_fonts(fonts)

    def load_speeds(self):
        bsize = self.constants['BLOCK_SIZE']
        self.event_state.set_verticle_speed(bsize)
        # self.event_state.set_horizontal_speed(bsize)

        
    


