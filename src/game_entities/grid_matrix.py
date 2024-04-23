class GridMatrix:
    def __init__(self, constants, event_state):
        self.constants = constants
        self.event_state = event_state

    def _create_grid(self, rows, cols, 
                    start_point_x, start_point_y,
                    block_size):
        grid_cells = []
        for _ in range(rows):
            grid_row = []
            sp_x = start_point_x
            for _ in range(cols):
                grid_row.append({"val":-1,
                                 "coords":{'x':sp_x,
                                           'y':start_point_y}})
                sp_x += block_size
            start_point_y += block_size
            grid_cells.append(grid_row)
        return grid_cells

    def load_grid(self):
        rows, cols = self.constants['GRID_BLOCKS']
        grid_coords = self.event_state.get_game_grid_coords()
        block_size = self.constants['BLOCK_SIZE']
        start_point_y = grid_coords[1] - (2 * block_size)
        start_point_x = grid_coords[0]
        rows += 2
        grid_cells = self._create_grid(rows, cols,
                                       start_point_x,
                                       start_point_y,
                                       block_size)
        self.event_state.set_grid_matrix(grid_cells)
        
