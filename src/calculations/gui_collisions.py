
class GuiCollisions:
    def __init__(self, constants, event_state):
        self.constants = constants
        self.event_state = event_state
        self.func_mapper = {0:self.main_menu_collisions,
                            4:self.game_screen_collisions}

    def main_menu_collisions(self, name):
        if name.lower() == "start":
            self.event_state.set_current_shape(None)
            self.event_state.set_bag_of_7(None)
            self.event_state.set_event_state(4)
            self.event_state.set_score(0)
            self.event_state.set_verticle_speed(self.constants['BLOCK_SIZE'])
            
        if name.lower() == "highscores":
            pass
        if name.lower() == "about":
            pass
        if name.lower() == "exit":
            self.event_state.set_running(False)
        
    def game_screen_collisions(self, name):
        if name.lower() == "exit":
            self.event_state.set_event_state(0)

    def mouse_down_collisions(self):
        state = self.event_state.get_event_state()
        rectangles = self.event_state.get_menu_rectangles()
        rectangles = rectangles[state]
        mouse_x, mouse_y = self.event_state.get_mouse_pos()
        for rect_data in rectangles:
            if rect_data["rect"].collidepoint(mouse_x, mouse_y):
                func_handle = self.func_mapper[state]
                func_handle(rect_data['name'])
            