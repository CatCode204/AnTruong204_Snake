import numpy as np
import pygame
import enum

class Direction(enum.Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    
#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Snake:
    def __init__(self,headX,headY):
        self.headX = headX
        self.headY = headY
        self.direction = Direction.RIGHT
        self.body = [(headX,headY)]
        self.checkEat = False

    def Move(self):
        if self.direction == Direction.UP:
            self.headY -= 1
        elif self.direction == Direction.DOWN:
            self.headY += 1
        elif self.direction == Direction.LEFT:
            self.headX -= 1
        elif self.direction == Direction.RIGHT:
            self.headX += 1
        self.body.insert(0,(self.headX,self.headY))
        if not self.checkEat: self.body.pop()
        else: self.checkEat = False

    def ChangeDirection(self,direction):
        if direction == Direction.UP and self.direction != Direction.DOWN:
            self.direction = direction
        elif direction == Direction.DOWN and self.direction != Direction.UP:
            self.direction = direction
        elif direction == Direction.LEFT and self.direction != Direction.RIGHT:
            self.direction = direction
        elif direction == Direction.RIGHT and self.direction != Direction.LEFT:
            self.direction = direction
    
    def CheckEat(self,foodPosition):
        if self.headX == foodPosition[0] and self.headY == foodPosition[1]:
            self.checkEat = True
            return True
        return False 

    def CheckCollision(self):
        for i in range(1,len(self.body)):
            if self.headX == self.body[i][0] and self.headY == self.body[i][1]:
                return True
        return False
    
    def Draw(self,screen,blockSize):
        for i in range(len(self.body)):
            pygame.draw.rect(screen,RED,(self.body[i][0]*blockSize,self.body[i][1]*blockSize,blockSize,blockSize))
        pygame.draw.rect(screen,GREEN,(self.headX*blockSize,self.headY*blockSize,blockSize,blockSize))