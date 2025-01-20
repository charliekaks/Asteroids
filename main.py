import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_time = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()
    player = Player(x,y)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        for update in updateable:
            update.update(dt)
        
        screen.fill("black")

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        time_pass = game_time.tick(60)
        dt = time_pass/1000
        



if __name__ == "__main__":
    main()