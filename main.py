import pygame
from world.world_grid import Grid, Tile
from character_controller.player import Player

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Desktop Farming')
clock = pygame.time.Clock()


test_grid = Grid(20, 20, (0, 0, 0), 3, 25, screen)
test_tile = Tile(test_grid, 1, 3, 25, 25, "sprites/Dirt/plain_dirt.png")
test_tile = Tile(test_grid, 1, 4, 25, 25, "sprites/Dirt/plain_dirt.png")
test_tile = Tile(test_grid, 2, 0, 25, 25, "sprites/Dirt/plain_dirt.png")
test_tile = Tile(test_grid, 1, 1, 25, 25, "sprites/Dirt/plain_dirt.png")
test_tile = Tile(test_grid, 2, 4, 25, 25, "sprites/Dirt/plain_dirt.png")
test_tile = Tile(test_grid, 1, 0, 25, 25, "sprites/Dirt/plain_dirt.png")
test_tile = Tile(test_grid, 1, 2, 25, 25, "sprites/Dirt/plain_dirt.png")
#test_player = Player("sprites/player/player_template.png", 20, 20, screen)
#test_player.set_position(0, 0)

print(test_grid.grid)

program_is_running = True
while program_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_is_running = False
            
    screen.fill((101, 163, 96))
    
    test_grid.show_grid_outline()
    #test_player.show_player()
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()