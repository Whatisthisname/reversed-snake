import threading
import pygame
import random
import numpy as np
from SnakeEnvironment import SnakeEnvironment 
import time

keypress : int

def main():
    global keypress

    keypress = 2
    gridsize = (20,20)
    # start
    print("started game")
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    screen.fill((100, 100, 120))
    pygame.display.set_caption('Snake')


    font = pygame.font.SysFont(pygame.font.get_default_font(), 40)
    
    # welcome the player:
    text = font.render("Welcome to Reverse snake!", True, (100, 255, 100))
    textRect = text.get_rect()
    textRect.center = (screen.get_width()//2,screen.get_height()//2)
    screen.blit(text, textRect)
    # pygame.event.pump()
    pygame.display.update()
    time.sleep(1)

    env = SnakeEnvironment(gridsize=gridsize)
    
    
    
    # running
    while(True):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            break
        if keys[pygame.K_LEFT]:
            keypress = 1
        elif keys[pygame.K_RIGHT]:
            keypress = 2
        elif keys[pygame.K_DOWN]:
            keypress = 3
        elif keys[pygame.K_UP]:
            keypress = 4
        
        state, reward, done = env.step(keypress)

        env.render(screen)
        pygame.event.pump()

        if (done):
            time.sleep(0.7)
            break
        
        time.sleep(1/10)

    # end
    print("ended game")
    pygame.display.quit()
    pygame.quit()
    exit()


def read_keypresses():
    global keypress

    while(True):
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    print("Keydown!", event.key)
                    if event.key == pygame.K_LEFT:
                        keypress = 1
                    elif event.key == pygame.K_RIGHT:
                        keypress = 2
                    elif event.key == pygame.K_DOWN:
                        keypress = 3
                    elif event.key == pygame.K_UP:
                        keypress = 4
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
        except Exception as e:
            pass

if __name__ == "__main__":
    main()