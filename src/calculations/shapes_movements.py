
def vertical_movement(event_state):
    pass

def horizontal_movement(event_state, speed):
    pass

def adjust_speeds(event_state, constants):
    movement_delays = constants['movement_delay']
    level = event_state.get_level()
    delay = movement_delays[level]
    return delay
