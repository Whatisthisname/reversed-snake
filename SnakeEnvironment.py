from typing import List, Tuple
import numpy as np
import pygame


class SnakeEnvironment:

    gridsize : Tuple[int, int]
    snake_length : int
    body = []
    pos : np.ndarray
    dir : np.ndarray
    food : np.ndarray

    def __init__(self, **args ) -> None:

        self.gridsize = args["gridsize"]
        self.reset()


    def reset(self) -> Tuple[np.ndarray, int, bool]: 
        self.snake_length = 1
        self.pos = np.array([0, 0])
        self.dir = np.array([1, 0])
        self.body = []
        self.food = np.random.randint(0, self.gridsize, size=2)
        return self.get_state(), 0, False


    def get_state(self) -> np.ndarray:
        s = np.zeros(self.gridsize)
        s[tuple(self.food)] = 1
        for pos in self.body:
            s[tuple(pos)] = 2
        return s


    def step(self, direction: int) -> Tuple[np.ndarray, int, bool]:



        # update snake direction
        if direction == 1:
            self.dir = np.array([-1, 0])
        elif direction == 2:
            self.dir = np.array([1, 0])
        elif direction == 3:
            self.dir = np.array([0, 1])
        elif direction == 4:
            self.dir = np.array([0, -1])
        elif direction == 0:
            self.dir = np.array([0, 0])

        
        self.body.append(tuple(self.pos))
        self.pos += self.dir

        # update snake body

        if len(self.body) > self.snake_length:
            self.body.pop(0)

        # check if snake is in self
        if tuple(self.pos) in self.body:
            print("snake is dead")
            return self.get_state(), -1, True

        # check if snake is out of bounds
        if self.pos[0] < 0 or self.pos[0] >= self.gridsize[0] or self.pos[1] < 0 or self.pos[1] >= self.gridsize[1]:
            print("snake is out of bounds")
            return self.get_state(), -1, True

        # check if snake has eaten food
        if tuple(self.pos) == tuple(self.food):
            print("ate food")
            self.snake_length += 1
            self.food = np.random.randint(0, self.gridsize, size=2)
            while tuple(self.food) in self.body:
                self.food = np.random.randint(0, self.gridsize, size=2)
            

        return self.get_state(), 1, False

    def render(self, screen : pygame.Surface): 
        screen.fill((100, 100, 120))
        
        size = 1
        screenSize = screen.get_size()
        w = screenSize[0] / self.gridsize[0]
        h = screenSize[1] / self.gridsize[1]
    
        # draw body
        for i, pos in enumerate(self.body):
            pygame.draw.rect(screen, (100, 200 + ((i%2) - 0.5 * 2) * 55, 100), (pos[0]*w, pos[1]*h, w, h))

        # draw head
        pygame.draw.rect(screen, (200, 255, 200), (self.body[0][0]*w + 0.25*w, self.body[0][1]*h + 0.25*h, w*0.5, h*0.5))

        # draw food
        pygame.draw.rect(screen, (255, 0, 0), (self.food[0]*w, self.food[1]*h, w, h))
        pygame.display.update()