from abc import ABC, abstractmethod
from ..calculations.dims import *
from ..services import read_files

class Screen(ABC):
    @abstractmethod
    def draw_screen(self):
        pass

    def draw_menu_boxes(self, menu_dict,
                        event_state,
                        item_name):
        container_cords = event_state.get_container_coords()
        width = menu_dict['box_dims']['width']
        height = menu_dict['box_dims']['height']
        x, y, width, height = calculate_menu_boxes\
            (menu_dict['coords'][item_name],
                                    container_cords, width, height)
        
        return x, y, width, height
    
    def get_title_coords(self, title_coords, event_state):
        x_off, y_off = title_coords['x_off'], title_coords['y_off']
        container_cords = event_state.get_container_coords()
        title_dims = calculate_title_coords(container_cords['cont_x'],
                                            container_cords['cont_y'],
                                            container_cords['cont_width'],
                                            container_cords['cont_height'],
                                            x_off, y_off)
        return title_dims
    

class Title:
    def __init__(self, font, colors, screen, event_state):
        self.font = font
        self.colors = colors
        self.screen = screen
        self.event_state = event_state

    def draw_title(self, text, coords):
        text_surface = self.font.render(text, True, self.colors)
        container_coords = self.event_state.get_container_coords()
        coords = calculate_title_coords(
                                        container_coords['cont_x'],
                                        container_coords['cont_y'],
                                        container_coords['cont_width'],
                                        container_coords['cont_height'],
                                        coords['x_off'], coords['y_off'])
        self.screen.blit(text_surface, coords)
