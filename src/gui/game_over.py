import pygame
from .screen_loader import Screen
from ..calculations.dims import *

class GameOver(Screen):
    def __init__(self, constants, event_state, screen, game):
        self.constants = constants
        self.event_state = event_state
        self.screen = screen
        self.game = game

    def blit_game_over(self):
        pass

    def blit_play_again(self):
        pass

    def blit_exit(self):
        pass

    def blit_highscore(self):
        pass

    def blit_enter_high_score_name(self):
        pass

    def blit_check_highscore(self):
        pass

    def draw_screen(self):
        pass