class GameCollisions:
    def __init__(self, event_state, constants):
        self.event_state = event_state
        self.grid_coords = event_state.get_game_grid_coords()
        self.constants = constants
        

    def check_game_over(self):
        pass

    def check_boundary(self):
        boundary_rect = self.event_state.get_boundary_rect()
        curr_shape = self.event_state.get_current_shape()
        if curr_shape == -1:
            return
        all_curr_rects = curr_shape.all_rects
        left_b = boundary_rect['left']
        right_b = boundary_rect['right']
        bottom_b = boundary_rect['bottom']
        for r in all_curr_rects:
            if r.colliderect(left_b):
                self.event_state.set_left_move(False)
                self.event_state.set_right_move(True)
                return
            if r.colliderect(right_b):
                self.event_state.set_right_move(False)
                self.event_state.set_left_move(True)
                return
            if r.colliderect(bottom_b):
                self.event_state.set_verticle_speed(0)
                return
                
        self.event_state.set_left_move(True)
        self.event_state.set_right_move(True)
        self.event_state.set_verticle_speed(self.constants['BLOCK_SIZE'])
