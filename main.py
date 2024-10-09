import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"checking variables from costants.py")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    print(f"init pygame")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"init clock") 
    tclock = pygame.time.Clock()
    dt = 0

    print(f"init player")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print(f"init game loop")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # print(f"drawing screen")
        screen.fill("black")
        player.draw(screen) 
        pygame.display.flip()
        # print(f"drawing player")

        dt = tclock.tick(60) / 1000




if __name__ == "__main__":
    main()
