from settings import *
from player import Player

class Game: 
    def __init__(self):
        # setup 
        pygame.init()
        self.display_surfface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Survivor")
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = pygame.sprites.Group()

        # sprites
        self.player = Player((400, 300), self.all_sprites)

    def run(self):
        while self.running:
            # dt
            dt = self.clock.tick() / 1000
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # update

            # draw
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()