import numpy as np
import pygame
import enum
import Snake
from Snake import *
import time

np.random.seed(np.random.randint(0,1000))

class Game:
    def __init__(self,screenWidth,screenHeight,blockSize):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.snake = Snake(screenWidth//2,screenHeight//2)
        self.foodPosition = (self.snake.headX,self.snake.headY)
        self.GenerateFood()
        self.score = 0
        self.blockSize = blockSize
    def Update(self):
        self.snake.Move()
        if self.snake.CheckEat(self.foodPosition):
            self.score += 1
            self.GenerateFood()
        if self.snake.CheckCollision() or self.snake.headX < 0 or self.snake.headX >= self.screenWidth or self.snake.headY < 0 or self.snake.headY >= self.screenHeight:
            return False
        return True
    def GenerateFood(self):
        while self.foodPosition in self.snake.body:
            self.foodPosition = (np.random.randint(0,self.screenWidth),np.random.randint(0,self.screenHeight))
    def Draw(self,screen):
        screen.fill(BLACK)
        for block in self.snake.body:
            pygame.draw.rect(screen,GREEN,(block[0]*self.blockSize,block[1]*self.blockSize,self.blockSize,self.blockSize))
        pygame.draw.rect(screen,RED,(self.foodPosition[0]*self.blockSize,self.foodPosition[1]*self.blockSize,self.blockSize,self.blockSize))
        font = pygame.font.Font("KnightWarrior-w16n8.otf",36)
        text = font.render("Score: " + str(self.score),True,WHITE)
        screen.blit(text,(10,10))
        pygame.display.flip()
    def GetInput(self,eventInput):
        if eventInput.type == pygame.KEYDOWN:
            if eventInput.key == pygame.K_UP:
                self.snake.ChangeDirection(Direction.UP)
            elif eventInput.key == pygame.K_DOWN:
                self.snake.ChangeDirection(Direction.DOWN)
            elif eventInput.key == pygame.K_LEFT:
                self.snake.ChangeDirection(Direction.LEFT)
            elif eventInput.key == pygame.K_RIGHT:
                self.snake.ChangeDirection(Direction.RIGHT)
    def Run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screenWidth*self.blockSize,self.screenHeight*self.blockSize))
        pygame.display.set_caption("Snake")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.GetInput(event)
            running = self.Update()
            self.Draw(screen)
            pygame.time.delay(100)
            #pygame.time.Clock().tick(60)
        pygame.quit()
    
if __name__ == "__main__":
    game = Game(40,40,20)
    game.Run()