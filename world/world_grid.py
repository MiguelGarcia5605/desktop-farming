import pygame
import numpy
from pathfinding.core.grid import Grid as PathfindingGrid
from pathfinding.finder.a_star import AStarFinder

class GameGrid:
    OUTLINE_COLOR = (0, 0, 0)
    OUTLINE_THICKNESS = 1
    TILE_SIZE = 25
    
    def __init__(self, rows, columns, screen):
        self.rows = rows
        self.columns = columns
        self.screen = screen
        self.grid_data = numpy.empty((self.columns, self.rows), dtype=object)
        
        for c in range(self.columns):
            for r in range(self.rows):
                self.grid_data[r, c] = []

    def draw_grid_outline(self):
        for c in range(self.columns):
            for r in range(self.rows):
                pygame.draw.rect(
                    self.screen, 
                    self.OUTLINE_COLOR, 
                    pygame.Rect(c * self.TILE_SIZE, r * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE), 
                    self.OUTLINE_THICKNESS)

    def render_grid(self):
        for c in range(self.columns):
            for r in range(self.rows):
                for obj in self.grid_data[r, c]:
                    self.screen.blit(obj.sprite, obj.sprite_rect)
                    
    def get_grid_position_from_screen_position(self, x, y):
        return x // self.TILE_SIZE, y // self.TILE_SIZE
    
    def generate_pathfinding_matrix(self):
        return numpy.ones((self.rows, self.columns), dtype=int)
    
    def compute_path(self, start, end):
        matrix = self.generate_pathfinding_matrix()
        pathfinding_grid = PathfindingGrid(matrix=matrix)
        finder = AStarFinder()
        return finder.find_path(pathfinding_grid.node(*start), pathfinding_grid.node(*end), pathfinding_grid)[0]
    
class GridTile:
    def __init__(self, game_grid, x_pos, y_pos, sprite_path):
        self.grid = game_grid.grid_data
        self.grid[x_pos, y_pos].append(self)
        self.sprite = pygame.image.load(sprite_path)
        self.sprite_rect = self.sprite.get_rect()
        self.sprite_rect.topleft = (x_pos * GameGrid.TILE_SIZE, y_pos * GameGrid.TILE_SIZE)

class Character:
    PATH_FRAME_DELAY = 6
    
    def __init__(self, game_grid, x_pos, y_pos, sprite_path):
        self.grid = game_grid.grid_data
        self.x = x_pos
        self.y = y_pos
        self.path = []
        self.path_frame_delay_counter = 0
        self.is_following_path = False
        self.grid[self.x, self.y].append(self)
        
        self.sprite = pygame.image.load(sprite_path)
        self.sprite_rect = self.sprite.get_rect()
        self.update_sprite_position()
            
    def update_sprite_position(self):
        center_x = self.x * GameGrid.TILE_SIZE + GameGrid.TILE_SIZE // 2
        center_y = self.y * GameGrid.TILE_SIZE + GameGrid.TILE_SIZE // 2
        self.sprite_rect.center = (center_x, center_y)

    def set_path(self, path):
        self.path = path

    def move_along_path(self):
        if self.path:
            next_step = self.path.pop(0)
            self.x, self.y = next_step
            self.update_sprite_position()
        else:
            self.is_following_path = False
