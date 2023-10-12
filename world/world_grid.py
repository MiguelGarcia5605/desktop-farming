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

        self.grid = numpy.empty((self.columns, self.rows), dtype=object)
    
    def show_grid_outline(self):
        for c in range(self.columns):
            for r in range(self.rows):
                if self.grid[r, c] != None:
                    tile = self.grid[r, c]
                    self.screen.blit(tile.sprite, tile.sprite_rect)
                pygame.draw.rect(self.screen, self.outline_color, pygame.Rect(\
                    c * self.tile_size, r * self.tile_size, self.tile_size, self.tile_size), self.outline_thickness)
                    
                
class Tile:
    def __init__(self, grid, grid_position_x, grid_position_y, sprite_width, sprite_height, sprite_path):
        self.grid = grid
        self.grid.grid[grid_position_x, grid_position_y] = self
        pygame.sprite.Sprite.__init__(self)
        self.grid_position_x = grid_position_x
        self.grid_position_y = grid_position_y
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.sprite = pygame.image.load(sprite_path)
        self.sprite_rect = self.sprite.get_rect()
        self.sprite_rect.center = (self.sprite_width // 2, self.sprite_height // 2)
        self.sprite_rect.update(self.grid_position_x * self.grid.tile_size,\
                                self.grid_position_y * self.grid.tile_size,\
                                self.sprite_width, self.sprite_height)
         