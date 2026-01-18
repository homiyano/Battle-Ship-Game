import pygame

class Ship:
    
    def __init__(self, ai_game):
        
        # ship position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # loading the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        
        # ship start position
        self.rect.midbottom = self.screen_rect.midbottom
        
        
    def blitme(self):
        # ship in current location
        self.screen.blit(self.image, self.rect)
        