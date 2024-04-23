import pygame
from ..calculations.dims import place_items_at_offset_percent, get_x_y_block_count

class Shape:
    def __init__(self, constants,
                event_state,screen,
                shape, shape_name, block_color,
                coords, curr_grid_col
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
        self.current_grid_row = 0
        self.current_grid_col = curr_grid_col

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
        
    def _add_shape_to_existing(self, 
                               event_state,
                               elapsed_seconds,
                               movement_delay,
                               current_shape):
        event_state.set_prev_movement(elapsed_seconds-movement_delay)
        event_state.set_current_shape(-1)
        event_state.set_existing_shapes(current_shape)
        
    def move_shape_down(self, grid_cells):
      event_state = self.event_state
      elapsed_seconds = event_state.get_elapsed_seconds()
      movement_delay = event_state.get_movement_delay()
      prev_movement = event_state.get_prev_movement()
      if(elapsed_seconds - prev_movement) >= movement_delay:
          self.current_grid_row += 1
          _, y_blocks = get_x_y_block_count(self)
          if self.current_grid_row + y_blocks <= len(grid_cells):
            self.coords[1] =\
                grid_cells[self.current_grid_row]\
                  [self.current_grid_col]['coords']['y']
            event_state.set_prev_movement(elapsed_seconds)
          else:
              self._add_shape_to_existing(event_state, elapsed_seconds,
                                          movement_delay, self)
      if self.coords[1] > 1000:
          self._add_shape_to_existing(event_state, elapsed_seconds,
                                          movement_delay, self)
    
    def move_shape_horizontal(self, grid_cells):
        event_state = self.event_state
        elapsed_seconds = event_state.get_elapsed_seconds()
        movement_delay = event_state.get_horiz_delay()
        prev_movement = event_state.get_prev_horiz_movement()
        if (elapsed_seconds - prev_movement) < movement_delay:
          return
        x_blocks, _ = get_x_y_block_count(self)
        if event_state.get_left_pressed():
            if self.current_grid_col > 0:
                self.current_grid_col -= 1
                self.coords[0] = grid_cells[self.current_grid_row]\
                                  [self.current_grid_col]['coords']['x']

        elif event_state.get_right_pressed():
            if (self.current_grid_col + x_blocks) < len(grid_cells[0]):
                self.current_grid_col += 1
                self.coords[0] = grid_cells[self.current_grid_row]\
                                  [self.current_grid_col]['coords']['x']
        event_state.set_prev_horiz_movement(elapsed_seconds)
        
        
