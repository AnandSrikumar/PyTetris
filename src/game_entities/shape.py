import pygame
from ..calculations.dims import place_items_at_offset_percent

class Shape:
    def __init__(self, constants,
                event_state,screen,
                shape, shape_name, block_color,
                coords
                ):
        self.constants = constants
        self.event_state = event_state
        self.shape_rotation = shape
        self.screen = screen
        self.current_rotation = 0
        self.block_color = block_color
        self.shape_name = shape_name
        self.coords = coords
        self.all_rects = None

    def draw_shape(self, shape=None, BLACK=None,
                   BLOCK_SIZE=None, x=None, y=None):
        if shape is None:
          shape = self.shape_rotation[self.shape_name][self.current_rotation%4]
          BLACK = self.shape_rotation['BLACK']
          BLOCK_SIZE = self.constants['BLOCK_SIZE']
          x, y = self.coords
        all_rects = []
        for row_index, row in enumerate(shape):
            for col_index, block in enumerate(row):
                if block == 1:
                    pygame.draw.rect(self.screen, self.block_color, 
                                     (x + col_index * BLOCK_SIZE,
                                       y + row_index * BLOCK_SIZE,
                                         BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, BLACK, 
                                     (x + col_index * BLOCK_SIZE, 
                                      y + row_index * BLOCK_SIZE,
                                        BLOCK_SIZE, BLOCK_SIZE), 1)
                    all_rects.append(
                        pygame.Rect(x + col_index * BLOCK_SIZE,
                                    y + row_index * BLOCK_SIZE,
                                    BLOCK_SIZE, BLOCK_SIZE)
                    )
        self.all_rects = all_rects
    
    def display_shape_in_next(self, y_off):
        shape = self.shape_rotation[self.shape_name][0]
        BLACK = self.shape_rotation['BLACK']
        BLOCK_SIZE = self.constants['BLOCK_SIZE']//2
        state = self.event_state.get_event_state()
        rects = self.event_state.get_menu_rectangles()
        rects = rects[state]
        rects = [x for x in rects if x['name']=="NEXT_SHAPE_CONTAINER"][0]['rect']
        cont_x, cont_y = rects.x, rects.y
        cont_width, cont_height = rects.width, rects.height
        x_off = 0.3
        x, y = place_items_at_offset_percent(cont_x,
                                             cont_y,
                                             cont_width,
                                             cont_height,
                                             x_off,
                                             y_off)
        self.draw_shape(shape=shape, BLACK=BLACK,
                        BLOCK_SIZE=BLOCK_SIZE,
                        x=x, y=y)
        
        
