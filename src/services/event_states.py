class EventVariables:
    def __init__(self):
        self._running = True
        self._container_coords = {}
        self._event_state = 3
        self._states = {0:"main_menu",
                       1:"highscore",
                       2:"pause_menu",
                       3:"game_over",
                       4:"game"}
        self._fonts = None
        self.event_objects = None
        self._menu_rectangles = None
        self._mouse_pos = None
        self._is_mouse_pressed = False
        self._score = 0
        self._bag_of_7 = None
        self._current_shape = None
        self._verticle_speed = 0
        self._horizontal_speed = 0
        self._fps = 60
        self._movement_delay = 400
        self._elapsed_seconds = 0
        self._prev_movement = 0
        self._level = 1
        self._left_pressed = False
        self._right_pressed = False
        self._horiz_delay = 60
        self._prev_horiz_mov = 0
        self._game_grid_coords = None
        self._boundary_states = None
        self._left_move = True
        self._right_move = True
        self._bottom_move = True
        self._grid_matrix = []
        self._existing_shapes = []
        self._game_over = False
        self._pause = False
    
    def set_pause(self, p):
        self._pause = p
    
    def get_pause(self):
        return self._pause

    def get_game_over(self):
        return self._game_over
    
    def set_game_over(self, gameover):
        self._game_over = gameover

    def set_existing_shapes(self, shape):
        self._existing_shapes.append(shape)

    def get_existing_shapes(self):
        return self._existing_shapes

    def set_grid_matrix(self, matrix):
        self._grid_matrix = matrix

    def get_grid_matrix(self):
        return self._grid_matrix

    def set_left_move(self, value):
        self._left_move = value

    def get_left_move(self):
        return self._left_move

    def set_right_move(self, value):
        self._right_move = value

    def get_right_move(self):
        return self._right_move

    def set_bottom_move(self, value):
        self._bottom_move = value

    def get_bottom_move(self):
        return self._bottom_move

    def set_boundary_rect(self, boundary):
        self._boundary_states = boundary

    def get_boundary_rect(self):
        return self._boundary_states

    def set_game_grid_coords(self, coords):
        self._game_grid_coords = coords

    def get_game_grid_coords(self):
        return self._game_grid_coords
    
    def get_prev_horiz_movement(self):
        return self._prev_horiz_mov
    
    def set_prev_horiz_movement(self, secs):
        self._prev_horiz_mov = secs

    def get_horiz_delay(self):
        return self._horiz_delay

    def set_left_pressed(self, l):
        self._left_pressed = l

    def get_left_pressed(self):
        return self._left_pressed
    
    def set_right_pressed(self, r):
        self._right_pressed = r

    def get_right_pressed(self):
        return self._right_pressed
    
    def set_level(self, level):
        self._level = level

    def get_level(self):
        return self._level

    def set_prev_movement(self, prev):
        self._prev_movement = prev
    
    def get_prev_movement(self):
        return self._prev_movement

    def set_elapsed_seconds(self, secs):
        self._elapsed_seconds = secs

    def get_elapsed_seconds(self):
        return self._elapsed_seconds

    def set_movement_delay(self, delay):
        self._movement_delay = delay

    def get_movement_delay(self):
        return self._movement_delay
    
    def get_fps(self):
        return self._fps

    def set_verticle_speed(self, speed):
        self._verticle_speed = speed

    def get_verticle_speed(self):
        return self._verticle_speed
    
    def set_horizontal_speed(self, speed):
        self._horizontal_speed = speed

    def get_horizontal_speed(self):
        return self._horizontal_speed
    
    def set_current_shape(self, shape):
        self._current_shape = shape

    def get_current_shape(self):
        return self._current_shape

    def set_score(self, score):
        self._score = score

    def get_score(self):
        return self._score
    
    def set_is_mouse_pressed(self, val: bool):
        self._is_mouse_pressed = val
    
    def get_is_mouse_pressed(self):
        return self._is_mouse_pressed

    def set_running(self, value: bool):
        self._running=value

    def get_running(self):
        return self._running
    
    def set_fonts(self, fonts):
        self._fonts = fonts

    def get_font(self, font_key, state):
        return self._fonts[font_key][state]

    def get_all_fonts(self):
        return self._fonts
    
    def set_container_coords(self, x, y, width, height):
        self._container_coords['cont_x'] = x
        self._container_coords['cont_y'] = y
        self._container_coords['cont_width'] = width
        self._container_coords['cont_height'] = height

    def get_container_coords(self):
        return self._container_coords
    
    def set_event_state(self, event_state):
        self._event_state = event_state

    def get_event_state(self):
        return self._event_state
    
    def get_all_event_states(self):
        return self._states
    
    def set_event_objects(self, event_objects):
        self.event_objects = event_objects
    
    def get_event_objects(self):
        return self.event_objects
    
    def set_menu_rectangles(self, rectangles, state):
        self._menu_rectangles = {state: rectangles}

    def get_menu_rectangles(self):
        return self._menu_rectangles
    
    def set_mouse_pos(self, mouse_pos):
        self._mouse_pos = mouse_pos

    def get_mouse_pos(self):
        return self._mouse_pos
    
    def set_bag_of_7(self, bag_of_seven):
        self._bag_of_7 = bag_of_seven

    def get_bag_of_7(self):
        return self._bag_of_7