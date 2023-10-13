import pygame
from world.world_grid import Grid, Tile, Player

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Desktop Farming')
clock = pygame.time.Clock()

test_grid = Grid(5, 5, (0, 0, 0), 1, 25, screen)

test_tile1 = Tile(test_grid, 2, 2, 25, 25, "sprites/Dirt/plain_dirt.png")
test_tile2 = Tile(test_grid, 2, 3, 25, 25, "sprites/Dirt/plain_dirt.png")
test_tile3 = Tile(test_grid, 3, 2, 25, 25, "sprites/Dirt/plain_dirt.png")
test_tile4 = Tile(test_grid, 3, 3, 25, 25, "sprites/Dirt/plain_dirt.png")
    
test_player = Player(test_grid, 2, 2, 20, 20, "sprites/player/player_template.png")

print(test_grid.grid[0, 0])

program_is_running = True
while program_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_is_running = False
            
    screen.fill((101, 163, 96))
    
    test_grid.show_grid_outline()
    test_grid.show_grid()
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()