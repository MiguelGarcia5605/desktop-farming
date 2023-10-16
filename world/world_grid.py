import pygame
import numpy
import math
from pathfinding.core.grid import Grid as PathfindingGrid
from pathfinding.finder.a_star import AStarFinder

class WorldGrid:
    outline_color = (0, 0, 0)
    outline_thickness = 1
    tile_size = 25
    
    def __init__(self, rows, columns, screen):
        self.rows = rows
        self.columns = columns
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
                    self.outline_thickness)

    def show_grid(self):
        for c in range(self.columns):
            for r in range(self.rows):
                for obj in self.grid[r, c]:
                    self.screen.blit(obj.sprite, obj.sprite_rect)
                    
    def mouse_pos_to_grid_pos(self, x, y):
        mouse_pos = [x, y]
        grid_pos = [0, 0]
        grid_pos[0] = math.floor(mouse_pos[0] / self.tile_size)
        grid_pos[1] = math.floor(mouse_pos[1] / self.tile_size)
        return grid_pos
    
    def get_pathfinding_matrix(self):
        matrix = numpy.ones((self.rows, self.columns), dtype=int)
        return matrix
    
    def find_path(self, starting_point, ending_point, matrix):
        grid = PathfindingGrid(matrix=matrix)

        starting_point = grid.node(starting_point[0], starting_point[1])
        ending_point = grid.node(ending_point[0], ending_point[1])
        
        finder = AStarFinder()
        path, _ = finder.find_path(starting_point, ending_point, grid)
        return path

class Tile:
    def __init__(self, grid, grid_position_x, grid_position_y, sprite_path):
        self.grid = grid.grid
        self.grid[grid_position_x, grid_position_y].append(self)
        self.sprite = pygame.image.load(sprite_path)
        self.sprite_rect = self.sprite.get_rect()
        self.sprite_rect.topleft = (grid_position_x * grid.tile_size, grid_position_y * grid.tile_size)

class Player:
    def __init__(self, grid, grid_position_x, grid_position_y, sprite_path):
        self.grid = grid.grid
        self.grid_position_x = grid_position_x
        self.grid_position_y = grid_position_y
        self.grid[grid_position_x, grid_position_y].append(self)
        self.sprite = pygame.image.load(sprite_path)
        self.sprite_rect = self.sprite.get_rect()
        self.sprite_rect.topleft = (grid_position_x * grid.tile_size, grid_position_y * grid.tile_size)
        cell_center_x = grid_position_x * grid.tile_size + grid.tile_size // 2
        cell_center_y = grid_position_y * grid.tile_size + grid.tile_size // 2
        self.sprite_rect.center = (cell_center_x, cell_center_y)
            
    def set_position(self, x, y):
        self.grid[self.grid_position_x, self.grid_position_y].remove(self)
        
        self.grid_position_x = x
        self.grid_position_y = y
        
        self.grid[self.grid_position_x, self.grid_position_y].append(self)
        
        cell_center_x = x * WorldGrid.tile_size + WorldGrid.tile_size // 2
        cell_center_y = y * WorldGrid.tile_size + WorldGrid.tile_size // 2
        self.sprite_rect.center = (cell_center_x, cell_center_y)
        
