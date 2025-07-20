# this allows us to use code from
# the open-source pygame libary
# throught this file
import pygame
from constants import *
from player import Player
#use this command to get uv to run the right packages source .venv/bin/activate
def main():
    pygame.init()
    PyClock = pygame.time.Clock()
    dt = 0 #I assume deltatime
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player( (SCREEN_WIDTH / 2), (SCREEN_HEIGHT /2) )

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {720}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #player.update(dt)
        updatable.update(dt)

        screen.fill
        #player.draw(screen)
        #drawable.draw(screen)
        for each in drawable:
            each.draw(screen)

        pygame.display.flip()
        dt = PyClock.tick(60) / 1000
        #PyClock.tick(60)




if __name__ == "__main__":
    main()
