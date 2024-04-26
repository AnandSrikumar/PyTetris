import pygame
from .screen_loader import Screen
from ..calculations.dims import *
from ..services.read_files import read_json
from ..game_entities.bag_of_seven import BagOfSeven
from ..game_entities.grid_matrix import GridMatrix
from ..calculations.shapes_calculations import detect_line_complete, detect_game_over


class GameScreen(Screen):
    def __init__(self, constants, title, game, event_state, screen,
                 game_collisions=None):
        self.constants = constants
        self.title = title
        self.game = game
        self.event_state = event_state
        self.screen = screen
        self.coords = self.event_state.get_container_coords()
        self.rectangles = []
        self.rectangle_menu_set = False
        self.game_collisions = game_collisions

    def load_shape_objects(self):
        shapes_file = self.constants['shapes']
        shapes_dict = read_json(shapes_file)
        state = self.event_state.get_event_state()
        coords = self.event_state.get_menu_rectangles()[state] #GAME_GRID
        grid_coords = [x['rect'] for x in coords if x['name']=="GAME_GRID"][0]
        grid_coords = [grid_coords.x, grid_coords.y,
                       grid_coords.width,
                       grid_coords.height]
        bag_of_seven = BagOfSeven(self.constants,
                                  self.event_state,
                                  self.screen,
                                  shapes_dict,
                                  grid_coords)
        self.event_state.set_bag_of_7(bag_of_seven)
        return bag_of_seven

    def scores_blit(self, font, color):
        scoring_title = self.game["score_title"]
        scoring = self.game['score']
        score_title_coords = place_items_at_offset_percent(self.coords['cont_x']
                                                    ,self.coords['cont_y']
                                                    ,self.coords['cont_width'],
                                                    self.coords['cont_height'],
                                                    scoring_title['x_off'],
                                                    scoring_title['y_off'])
        score_coords = place_items_at_offset_percent(self.coords['cont_x']
                                                    ,self.coords['cont_y']
                                                    ,self.coords['cont_width'],
                                                    self.coords['cont_height'],
                                                    scoring['x_off'],
                                                    scoring['y_off'])
        score = self.event_state.get_score()
        text_surface = font.render('SCORE', True, color)
        score_surface = font.render(str(score), True, color)
        self.screen.blit(text_surface, score_title_coords)
        self.screen.blit(score_surface, score_coords)

    def grid_blit(self, grid_boundary_color, block_size):
        rows, cols = self.game['rows'], self.game['cols']
        grid_dims = calculate_grid_dims(self.coords['cont_x']
                                        ,self.coords['cont_y']
                                        ,self.coords['cont_width'],
                                        self.coords['cont_height'],
                                        block_size, rows, cols
                                        )
        x, y, width, height = grid_dims
        pygame.draw.rect(self.screen, grid_boundary_color,
                         (x-1, y-1, width+1, height+1),
                         width=1)
        self.rectangles.append({"rect":pygame.Rect(x-1, y-1, width+1, height+1),
                               "name":'GAME_GRID'})
        self.event_state.set_game_grid_coords([x, y, width, height])
        
    def grid_exit_blit(self, color, font):
        self.game['coords'] = {}
        self.game['coords']['EXIT'] = self.game['exit']
        x, y, width, height = self.draw_menu_boxes(self.game,
                                                    self.event_state, 'EXIT')
        pygame.draw.rect(self.screen, color,
                            (x, y, width, height),
                            width=self.game['box_line_width'])
        self.rectangles.append({"rect":pygame.Rect(x, y, width, height),
                               "name":'EXIT'})
        text_surface = font.render('EXIT', True, color)
        name_coords = center_elements(x, y, width, height,
                                        text_surface.get_width(),
                                        text_surface.get_height())
        self.screen.blit(text_surface, name_coords)
        
    def shape_blit(self, color, block_size, font):
        next_shapes_container = self.game['next_shapes_container']
        rows, cols = 8, 8
        x, y = place_items_at_offset_percent(self.coords['cont_x']
                                    ,self.coords['cont_y']
                                    ,self.coords['cont_width'],
                                    self.coords['cont_height'],
                                    next_shapes_container['x_off'],
                                    next_shapes_container['y_off'])
        width = block_size * rows
        height = block_size * cols

        next_shapes = self.game['next_shapes']
        x_t, y_t = place_items_at_offset_percent(self.coords['cont_x']
                                ,self.coords['cont_y']
                                ,self.coords['cont_width'],
                                self.coords['cont_height'],
                                next_shapes['x_off'],
                                next_shapes['y_off'])
        pygame.draw.rect(self.screen, next_shapes_container['color'],
                         (x, y, width, height),
                         width=2)
        self.rectangles.append({"rect":pygame.Rect(x, y, width, height),
                               "name":'NEXT_SHAPE_CONTAINER'})
        text_surface = font.render('NEXT', True, color)
        self.screen.blit(text_surface, (x_t, y_t))

    def game_over_state_change(self):
        game_over = self.event_state.get_game_over()
        if game_over:
            self.event_state.set_state(3)

    def pause_text_blit(self, font, color):
        x, y, width, height = self.event_state.get_game_grid_coords()
        px, py = place_items_at_offset_percent(x, y, width, height, 0.25, 0.4)
        text_surface = font.render('PAUSED', True, color)
        self.screen.blit(text_surface, (px, py))


    def game_object_blit(self, grid_rows, font, color):
        if self.event_state.get_pause():
            self.pause_text_blit(font, color)
            return
        self.game_over_state_change()
        curr_shape = self.event_state.get_current_shape()
        b7 = self.event_state.get_bag_of_7()
        if curr_shape is None:
            b7 = self.load_shape_objects()
            b7.load_seven(grid_rows[0])
            b7.append_queue()
            shape = b7.get_queue_element()
            self.event_state.set_current_shape(shape)
        
        if len(b7.seven) == 0:
            b7.load_seven(grid_rows[0])
        
        if curr_shape == -1:
            shape = b7.get_queue_element()
            self.event_state.set_current_shape(shape)

        self.event_state.get_current_shape().draw_shape()

    def next_shapes_blit(self):
        b7 = self.event_state.get_bag_of_7()
        queue_3 = b7.queue[0:3]
        y_off = 0.1
        for q in queue_3:
            q.display_shape_in_next(y_off)
            y_off += 0.3
    
    def existing_shapes_blit(self):
        existing_shapes = self.event_state.get_existing_shapes()
        for shape in existing_shapes:
            shape.draw_shape()
    
    def movements(self, grid_rows):
        current_shape = self.event_state.get_current_shape()
        if current_shape == -1:
            return
        current_shape.move_shape_down(grid_rows)
        current_shape.move_shape_horizontal(grid_rows)

    def draw_existing_shapes(self, grid):
        block_size = self.constants['BLOCK_SIZE']
        BLACK = self.constants['GAME_CONTAINER_COLOR']
        for row in grid:
            for col in row:
                val = col['val']
                if val == -1:
                    continue
                x, y = col['coords']['x'], col['coords']['y']
                color = col['color']
                pygame.draw.rect(self.screen,
                                 color,
                                 (x, y, block_size, block_size),
                                 )
                pygame.draw.rect(self.screen,
                                 BLACK,
                                 (x, y, block_size, block_size),
                                 1
                                 )
                
    def preloader(self):
        existing_rects = self.event_state.get_menu_rectangles().get(4)
        if not self.rectangle_menu_set or existing_rects is None:
            self.event_state.set_menu_rectangles(self.rectangles,
                                        self.event_state.get_event_state())
            gmatrix = GridMatrix(self.constants, self.event_state)
            gmatrix.load_grid()
            self.rectangle_menu_set = True
            self.rectangles = []

    def draw_screen(self):
        font = self.event_state.get_all_fonts()['text_font']
        color = self.game['font_color']
        grid_boundary_color = self.game['grid_boundary_color']
        block_size = self.game['block_size']
        self.scores_blit(font, color)
        self.grid_blit(grid_boundary_color, block_size)
        self.shape_blit(color, block_size, font)
        self.grid_exit_blit(color, font)
        self.preloader()
        grid_rows = self.event_state.get_grid_matrix()
        self.game_object_blit(grid_rows, font, color)
        # self.existing_shapes_blit()
        self.draw_existing_shapes(grid_rows)
        self.movements(grid_rows)
        self.next_shapes_blit()
        self.event_state.set_game_over(detect_game_over(grid_rows))
        detect_line_complete(grid_rows, self.event_state, self.constants)
        self.event_state.set_game_over(detect_game_over(grid_rows))
        
