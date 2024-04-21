
import random

def place_item_at_screen_center(screen_width, screen_height,
                                 entity_width,
                                   entity_height,
                                     padding=5,
                                     x_start=0,
                                     y_start=0):
    horiz_center = screen_width//2
    vert_center = screen_height//2
    x_origin = horiz_center - (entity_width//2)
    x_origin += x_start
    y_origin = vert_center - (entity_height//2)
    y_origin += y_start
    return x_origin, y_origin, entity_width, entity_height

def calculate_grid_dims(container_origin_x,
                        container_origin_y,
                        container_width,
                        container_height,
                        block_size,
                        grid_rows,
                        grid_cols,
                        ):
    width = grid_cols * block_size
    height = grid_rows * block_size
    place_dims = place_item_at_screen_center(container_width, 
                                             container_height,
                                             width,
                                             height,
                                             x_start=container_origin_x,
                                             y_start=container_origin_y)
    place_dims = [int(x) for x in place_dims]
    return place_dims

def get_boundary_dims(x, y, w, h, lw):
    boundary = {"width": lw,
                'boundary':[x, y, w, h]}
    return boundary
    
def calculate_boundaries_container(grid_x,
                                  grid_y,
                                  grid_width,
                                  grid_height):
    left_boundary = 0
    right_boundary = grid_x + grid_width
    start_y = grid_y
    block_size = grid_x
    boundaries = []
    while start_y <= grid_height:
        boundary_l1 = get_boundary_dims(left_boundary,
                                        start_y,
                                        block_size,
                                        block_size,
                                        1)
        boundary_l2 = get_boundary_dims(left_boundary+1, start_y+1,
                                        block_size-1, block_size-1, 0)
        boundary_r1 = get_boundary_dims(right_boundary, start_y,
                                        block_size, block_size, 1)
        boundary_r2 = get_boundary_dims(right_boundary+1, start_y+1,
                                        block_size-1, block_size-1, 0)
        boundaries.extend([boundary_l1, boundary_l2,
                          boundary_r1, boundary_r2])
        start_y += block_size
    return boundaries

def calculate_title_coords(grid_x,
                           grid_y,
                           grid_width,
                           grid_height,
                           x_off, y_off):
    x = grid_x + (grid_width*x_off)
    y = grid_y + (grid_height*y_off)
    return x, y

def center_elements(cont_x, cont_y,
                       cont_width, cont_height,
                       element_width, element_height):
    x_center = cont_x + cont_width//2
    x = x_center - element_width//2
    y_center = cont_y + cont_height//2
    y = y_center - element_height//2
    return x, y

def place_items_at_offset_percent(cont_x,
                                  cont_y,
                                  cont_width,
                                  cont_height,
                                  x_off,
                                  y_off):
    x = cont_x + (cont_width * x_off)
    y = cont_y + (cont_height * y_off)
    return x, y

def calculate_menu_boxes(menu, container_dims, width, height):
    x_cont, y_cont = container_dims['cont_x'], container_dims['cont_y']
    x_menu, y_menu = menu['x_off'], menu['y_off']
    w_container, h_container = container_dims['cont_width'],\
          container_dims['cont_height']
    x = x_cont + (w_container * x_menu)
    y = y_cont + (h_container * y_menu)
    width = w_container * width
    height = h_container * height
    return x, y, width, height

def calculate_shape_pos(container_coords, block_size):
    x_min = container_coords[0]
    x_max = (container_coords[0] + container_coords[2]) - (4*block_size)
    random_number = random.randint(x_min, x_max)
    
    # Calculate the remainder when dividing by the multiple
    remainder = random_number % block_size
    
    # Adjust the random number to be a multiple of the given multiple
    if remainder != 0:
        random_number += (block_size - remainder)
    
    return random_number


