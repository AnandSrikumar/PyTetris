
def vertical_movement(event_state):
    speed = event_state.get_verticle_speed()
    current_shape = event_state.get_current_shape()
    elapsed_seconds = event_state.get_elapsed_seconds()
    movement_delay = event_state.get_movement_delay()
    prev_movement = event_state.get_prev_movement()
    if(elapsed_seconds - prev_movement) >= movement_delay:
        current_shape.coords[1] += speed
        event_state.set_prev_movement(elapsed_seconds)
    if current_shape.coords[1] > 1000:
        event_state.set_prev_movement(elapsed_seconds-movement_delay)
        event_state.set_current_shape(-1)

def horizontal_movement(event_state, speed):
    current_shape = event_state.get_current_shape()
    elapsed_seconds = event_state.get_elapsed_seconds()
    movement_delay = event_state.get_horiz_delay()
    prev_movement = event_state.get_prev_horiz_movement()
    left_move = event_state.get_left_move()
    right_move = event_state.get_right_move()
    if current_shape == -1:
        return
    if (elapsed_seconds - prev_movement) < movement_delay:
        return
    if event_state.get_left_pressed() and left_move:
        current_shape.coords[0] -= speed
    elif event_state.get_right_pressed() and right_move:
        current_shape.coords[0] += speed
    event_state.set_prev_horiz_movement(elapsed_seconds)

def adjust_speeds(event_state, constants):
    movement_delays = constants['movement_delay']
    level = event_state.get_level()
    delay = movement_delays[level]
    return delay
