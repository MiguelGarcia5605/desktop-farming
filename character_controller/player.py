import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, player_sprite_path, player_width, player_height, screen):
        pygame.sprite.Sprite.__init__(self)
        self.player_width = player_width
        self.player_height = player_height
        self.player_sprite = pygame.image.load(player_sprite_path)
        self.player_sprite_rect = self.player_sprite.get_rect()
        #self.player_sprite_rect.center = (self.player_width // 2, self.player_height // 2)
        self.screen = screen
        
    def show_player(self):
        self.screen.blit(self.player_sprite, self.player_sprite_rect)
        
    def set_position(self, x, y):
        self.player_sprite_rect.update(x, y, self.player_width, self.player_height)