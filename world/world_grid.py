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
        for c in range(self.columns):
            for r in range(self.rows):
                self.grid[r, c] = []


    def show_grid_outline(self):
        for c in range(self.columns):
            for r in range(self.rows):
                pygame.draw.rect(
                    self.screen, 
                    self.outline_color, 
                    pygame.Rect(c * self.tile_size, r * self.tile_size, self.tile_size, self.tile_size), 
                    self.outline_thickness
                )

    def show_grid(self):
        for c in range(self.columns):
            for r in range(self.rows):
                for obj in self.grid[r, c]:
                    self.screen.blit(obj.sprite, obj.sprite_rect)

class Tile:
    def __init__(self, grid, grid_position_x, grid_position_y, sprite_width, sprite_height, sprite_path):
        self.grid = grid.grid
        self.grid[grid_position_x, grid_position_y].append(self)
        self.sprite = pygame.image.load(sprite_path)
        self.sprite_rect = self.sprite.get_rect()
        self.sprite_rect.topleft = (grid_position_x * grid.tile_size, grid_position_y * grid.tile_size)

class Player:
    def __init__(self, grid, grid_position_x, grid_position_y, sprite_width, sprite_height, sprite_path):
        self.grid = grid.grid
        self.grid[grid_position_x, grid_position_y].append(self)
        self.sprite = pygame.image.load(sprite_path)
        self.sprite_rect = self.sprite.get_rect()
        self.sprite_rect.topleft = (grid_position_x * grid.tile_size, grid_position_y * grid.tile_size)