import pygame
from world.world_grid import WorldGrid, Tile, Player

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Desktop Farming')
clock = pygame.time.Clock()

test_grid = WorldGrid(20, 20, screen)
path = test_grid.find_path((0,0), (4, 1), test_grid.get_pathfinding_matrix())
print(path)
test_player = Player(test_grid, 2, 2, "sprites/player/player_template.png")

program_is_running = True
while program_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]
            click_grid_pos = test_grid.mouse_pos_to_grid_pos(mouse_x, mouse_y)
            test_player.set_position(click_grid_pos[0], click_grid_pos[1])
            
    screen.fill((100, 150, 100))
    
    test_grid.show_grid_outline()
    test_grid.show_grid()
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()