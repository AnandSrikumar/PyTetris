import pygame
from .screen_loader import Screen
from ..calculations.dims import *

class MainMenu(Screen):
    def __init__(self, constants, title, menu, event_state, screen):
        self.constants = constants
        self.title = title
        self.menu = menu
        self.event_state = event_state
        self.screen = screen
    
    def draw_screen(self):
        elements = self.menu['elements']
        font = self.event_state.get_all_fonts()['other_fonts']
        rectangles = []
        for idx, v in enumerate(elements):
            x, y, width, height = self.draw_menu_boxes(self.menu,
                                                    self.event_state, v)
            color = self.menu['font_color']
            pygame.draw.rect(self.screen, color,
                            (x, y, width, height),
                            width=self.menu['box_line_width'])
            text_surface = font.render(v, True, color)
            name_coords = center_elements(x, y, width, height,
                                        text_surface.get_width(),
                                        text_surface.get_height())
            self.screen.blit(text_surface, name_coords)
            rectangles.append({"rect":pygame.Rect(x, y, width, height),
                               "name":v})
            self.event_state.set_menu_rectangles(rectangles,
                                                self.event_state.get_event_state())
            
        title_coords = self.menu['title_coords']
        self.title.draw_title("Tetris", title_coords)
