import pygame
import numpy

class Grid:
    def __init__(self, rows, columns, outline_color, outline_thickness, tile_size, screen):
        self.rows = rows
        self.columns = columns
        self.outline_color = outline_color
        self.outline_thickness = outline_thickness
        self.tile_size = tile_size
        self.screen = screen

        self.grid = numpy.zeros((self.columns, self.rows))
        print(self.grid)
    
    def show_grid_outline(self):
        for c in range(self.columns):
            for r in range(self.rows):
                pygame.draw.rect(self.screen, self.outline_color, pygame.Rect(\
                    c * self.tile_size, r * self.tile_size, self.tile_size, self.tile_size), self.outline_thickness)