from .shape import Shape
from ..services import read_files
from ..calculations.dims import *
import random

class BagOfSeven:
    def __init__(self, 
                 constants, 
                 event_state,
                 screen,
                 shapes,
                 container_coords):
        self.constants = constants
        self.shape_rotations = shapes
        self.queue = []
        self.seven = []
        self.event_state = event_state
        self.screen = screen
        self.container_coords = container_coords

    def load_seven(self):
        for k, v in self.shape_rotations.items():
            if k == "BLACK":
                continue
            random_color = random.choice(self.constants['RANDOM_COLORS'])
            block_size = self.constants['BLOCK_SIZE']
            random_pos = calculate_shape_pos(self.container_coords, block_size)
            blit_coords = [random_pos, self.container_coords[1]-block_size]
            shape_obj = Shape(self.constants,
                              self.event_state,
                              self.screen,
                              self.shape_rotations,
                              k,
                              random_color,
                              blit_coords
                              )
            self.seven.append(shape_obj)
        self.seven  = random.sample(self.seven, len(self.seven))
    
    def append_queue(self):
        if len(self.queue) == 0:
            for x in range(0, 3):
                self.queue.append(self.seven[x])
            del self.seven[0: 3]
            return
        self.queue.append(self.seven[0])
        del self.seven[0]

    def get_queue_element(self):
        element = self.queue[0]
        del self.queue[0]
        self.append_queue()
        return element