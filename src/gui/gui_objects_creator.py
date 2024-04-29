from .main_menu import MainMenu
from .game_screen import GameScreen
from .game_over import GameOver
from ..services import read_files
from ..calculations.game_collisions import GameCollisions

class LoadScreenState:
    def __init__(self, constants, title, event_state, screen):
        self.constants = constants
        self.title = title
        self.event_state = event_state
        self.screen = screen

    def create_state_objects(self):
        all_states = self.event_state.get_all_event_states()
        event_objects = {}
        for k, v in all_states.items():
            try:
                screen_path = self.constants[v]
                entity_dict = read_files.read_json(screen_path)
                if v == "main_menu":
                    state_obj = MainMenu(self.constants, self.title, entity_dict,
                                        self.event_state, self.screen)
                elif v == "game":
                    collisions = GameCollisions(self.event_state,
                                                self.constants)
                    state_obj = GameScreen(self.constants, self.title, entity_dict,
                                        self.event_state, self.screen, collisions)
                elif v == "game_over":
                    state_obj = GameOver(self.event_state, self.constants,
                                         self.screen, entity_dict)
                event_objects[v] = state_obj
            except Exception as e:
                print(str(e))
        self.event_objects = event_objects
        self.event_state.set_event_objects(event_objects)

    def draw_state(self):
        state = self.event_state.get_event_state()
        state_name = self.event_state.get_all_event_states()[state]
        state_obj = self.event_objects[state_name]
        state_obj.draw_screen()