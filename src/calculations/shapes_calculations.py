
def adjust_speeds(event_state, constants):
    movement_delays = constants['movement_delay']
    level = event_state.get_level()
    delay = movement_delays[level]
    return delay

def lines_rem(grid_cells, lines_idx):
    if len(lines_idx) == 0:
        return
    for idx in lines_idx:
        for col in range(len(grid_cells[0])):
            grid_cells[idx][col]['val'] = -1
            grid_cells[idx][col]['color'] = None
    move_down_idx = lines_idx[0]-1
    # for x in range(move_down_idx, 1, -1):
    #     grid_cells[x+1] = grid_cells[x]

def detect_line_complete(grid_cells):
    line_completes = 0
    line_rows_idx = []
    for idx, row in enumerate(grid_cells):
        complete = True
        for col in row:
            if col['val'] == -1:
                complete = False
                break
        if complete:
            line_completes += 1
            line_rows_idx.append(idx)
    lines_rem(grid_cells, line_rows_idx)

