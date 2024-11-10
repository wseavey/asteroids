# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from textbox import Textbox

def main():
    #setup screen, text, and clock settings
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #setup groups for sprites
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #assign containers to classes
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Textbox.containers = (updatable, drawable)

    #create field and player
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    title = Textbox(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, TITLE_TEXT)

    #main game loop
    while True:
        #quitting
        if Exception == True:
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise Exception
        
        #background
        screen.fill("black")

        #textboxes
        
        #loop over updateables
        for object in updatable:
            object.update(dt)

        #check for collisions
        for asteroid in asteroids:
            if asteroid.collisioncheck(player):
                deathscreen = Textbox(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, DEATH_TEXT)
                player.pause = True
                main()

            for shot in shots:
                if asteroid.collisioncheck(shot):
                    player.score += 1
                    asteroid.split()
                    shot.kill()

        #draw sprites
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        #framerate
        if player.pause:
            dt = 0
        else:
            dt = clock.tick(60) / 1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()