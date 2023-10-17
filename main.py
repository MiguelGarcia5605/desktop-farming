import pygame
from world.world_grid import GameGrid, GridTile, Character

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Desktop Farming')
clock = pygame.time.Clock()

game_grid = GameGrid(20, 20, screen)
player = Character(game_grid, 2, 2, "sprites/player/player_template.png")

program_is_running = True
while program_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = pygame.mouse.get_pos()
            start = (player.x, player.y)
            end = game_grid.get_grid_position_from_screen_position(click_x, click_y)
            path = game_grid.compute_path(start, end)
            player.set_path(path)
            player.is_following_path = True
            
    screen.fill((100, 150, 100))
    
    game_grid.draw_grid_outline()
    game_grid.render_grid()
    
    print(player.is_following_path)
    
    if(player.is_following_path):
        if(player.path_frame_delay_counter >= player.PATH_FRAME_DELAY):
            player.move_along_path()
            player.path_frame_delay_counter = 0
        else:
            player.path_frame_delay_counter += 1
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
