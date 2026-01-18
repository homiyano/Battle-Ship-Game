import sys

import pygame

from settings import Settings

class AlienInvasion:
    # managing game assets and behavior
    
    def __init__(self):
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        
        pygame.display.set_caption("Alien Invasion")
        
        # background color
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            pygame.display.flip()
            self.clock.tick(60)
            
            # background of game
            self.screen.fill(self.settings.bg_color)
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()