
def adjust_speeds(event_state, constants):
    movement_delays = constants['movement_delay']
    level = event_state.get_level()
    delay = movement_delays[level]
    return delay

def lines_rearrangement(grid_cells, lines_idx):
    for idx in lines_idx:
        move_down_idx = idx-1
        for x in range(move_down_idx, 1, -1):
            for col in range(len(grid_cells[0])):
                curr_col = grid_cells[x][col].get('color')
                curr_val = grid_cells[x][col]['val']
                grid_cells[x+1][col]['val'] = curr_val
                grid_cells[x+1][col]['color'] = curr_col
        
def lines_rem(grid_cells, lines_idx):
    if len(lines_idx) == 0:
        return
    for idx in lines_idx:
        for col in range(len(grid_cells[0])):
            grid_cells[idx][col]['val'] = -1
            grid_cells[idx][col]['color'] = None
    
    lines_rearrangement(grid_cells, lines_idx)
    # for x in range(move_down_idx, 1, -1):
    #     grid_cells[x+1] = grid_cells[x]

def detect_line_complete(grid_cells, event_state, constants):
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
    score_calculator(event_state, constants, 'lines', line_completes)

def detect_game_over(grid_cells):
    start = 0
    for idx, row in enumerate(grid_cells):
        for col in row:
            if col['val'] == 1:
                return True
        start += 1
        if start >= 2:
            break
    return False

def score_calculator(event_state, constants,
                    scoring_type='placed',
                    lines_cleared=None):
    level = event_state.get_level()
    score_val = constants['scores_awarded'][level]
    curr_score = event_state.get_score()
    if scoring_type == 'placed':
        movement_delay = constants['movement_delay'][level]
        placed = 'placed'
        if event_state.get_movement_delay() < movement_delay:
            placed = 'placed_fast'
        event_state.set_score(curr_score + score_val[placed])
    else:
        lc_score = score_val['lines'].get(lines_cleared, 0)
        event_state.set_score(curr_score + int(lc_score))



