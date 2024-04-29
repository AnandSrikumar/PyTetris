import pygame
from .screen_loader import Screen
from ..calculations.dims import *

class GameOver(Screen):
    def __init__(self, event_state,constants, screen, game):
        self.constants = constants
        self.event_state = event_state
        self.screen = screen
        self.game = game
        self.rectangles = []

    def blit_game_over(self, grid_coords, font, color):
        cx, cy = grid_coords['cont_x'], grid_coords['cont_y']
        cw, ch = grid_coords['cont_width'], grid_coords['cont_height']
        x_off = self.game['game_over_text']['x_off']
        y_off = self.game['game_over_text']['y_off']
        x, y = place_items_at_offset_percent(cx, cy,
                                             cw, ch,
                                             x_off, y_off)
        text_surface = font.render('GAME OVER', True, color)
        self.screen.blit(text_surface, (x, y))

    def blit_buttons(self, grid_coords, font, color,
                     button_name,
                     button_text):
        menu = self.game[button_name]
        box_dims = self.game['box_dims']
        x, y, width, height = calculate_menu_boxes(menu, grid_coords,
                                                    box_dims['width'], 
                                                    box_dims['height'])
        pygame.draw.rect(self.screen, color,
                            (x, y, width, height),
                            width=self.game['box_line_width'])
        text_surface = font.render(button_text, True, color)
        name_coords = center_elements(x, y, width, height,
                                        text_surface.get_width(),
                                        text_surface.get_height())
        self.screen.blit(text_surface, name_coords)
        self.rectangles.append({"rect":pygame.Rect(x, y, width, height),
                               "name":button_name})
        self.event_state.set_menu_rectangles(self.rectangles,
                                                self.event_state.get_event_state())

    def blit_highscore(self):
        pass

    def blit_enter_high_score_name(self):
        pass

    def blit_check_highscore(self):
        pass

    def draw_screen(self):
        grid_coords = self.event_state.get_container_coords()
        color = self.game['font_color']
        font = self.event_state.get_all_fonts()['text_font']
        self.blit_game_over(grid_coords, font, color)
        self.blit_buttons(grid_coords, font, color,
                          'play_again',
                          'Play Again')
        self.blit_buttons(grid_coords, font, color,
                          'exit',
                          'Exit')