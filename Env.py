import numpy as np
import pygame
import enum
from Snake import *
from Game import *

np.random.seed(np.random.randint(0,1000))

class Env:
    def __init__(self,screenWidth,screenHeight,blockSize):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.blockSize = blockSize
        self.game = Game(screenWidth,screenHeight,blockSize)
    def Reset(self):
        self.game = Game(self.screenWidth,self.screenHeight,self.blockSize)
        return self.GetState()
    def GetState(self):
        snake = self.game.snake
        food = self.game.foodPosition
        #State: [isFoodAhead,isFoodRight,isFoodLeft,isDangerAhead,isDangerRight,isDangerLeft]
        state = [0]*6
        if snake.direction == Direction.UP:
            if food[1] < snake.headY: state[0] = 1
            if food[0] > snake.headX: state[1] = 1
            if food[0] < snake.headX: state[2] = 1
            if snake.headY == 0 or (snake.headX,snake.headY-1) in snake.body: state[3] = 1
            if snake.headX + 1 >= self.screenWidth or (snake.headX+1,snake.headY) in snake.body: state[4] = 1
            if snake.headX == 0 or (snake.headX-1,snake.headY) in snake.body: state[5] = 1
        elif snake.direction == Direction.DOWN:
            if food[1] > snake.headY: state[0] = 1
            if food[0] < snake.headX: state[1] = 1
            if food[0] > snake.headX: state[2] = 1
            if snake.headY + 1 >= self.screenHeight or (snake.headX,snake.headY+1) in snake.body: state[3] = 1
            if snake.headX == 0 or (snake.headX-1,snake.headY) in snake.body: state[4] = 1
            if snake.headX + 1 >= self.screenWidth or (snake.headX+1,snake.headY) in snake.body: state[5] = 1
        elif snake.direction == Direction.LEFT:
            if food[0] < snake.headX: state[0] = 1
            if food[1] < snake.headY: state[1] = 1
            if food[1] > snake.headY: state[2] = 1
            if snake.headX == 0 or (snake.headX-1,snake.headY) in snake.body: state[3] = 1
            if snake.headY == 0 or (snake.headX,snake.headY-1) in snake.body: state[4] = 1
            if snake.headY + 1 >= self.screenHeight or (snake.headX,snake.headY+1) in snake.body: state[5] = 1
        elif snake.direction == Direction.RIGHT:
            if food[0] > snake.headX: state[0] = 1
            if food[1] > snake.headY: state[1] = 1
            if food[1] < snake.headY: state[2] = 1
            if snake.headX + 1 >= self.screenWidth or (snake.headX+1,snake.headY) in snake.body: state[3] = 1
            if snake.headY + 1 >= self.screenHeight or (snake.headX,snake.headY+1) in snake.body: state[4] = 1
            if snake.headY == 0 or (snake.headX,snake.headY-1) in snake.body: state[5] = 1
        return state
    def Step(self,action):
        """
        GET ACTION FROM [0,1,2]:
        0: Turn Left
        1: Keep Straight
        2: Turn Right
        """
        if action == 0:
            if (self.game.snake.direction == Direction.UP): self.game.snake.ChangeDirection(Direction.LEFT)
            elif (self.game.snake.direction == Direction.DOWN): self.game.snake.ChangeDirection(Direction.RIGHT)
            elif (self.game.snake.direction == Direction.LEFT): self.game.snake.ChangeDirection(Direction.DOWN)
            elif (self.game.snake.direction == Direction.RIGHT): self.game.snake.ChangeDirection(Direction.UP)
        elif action == 1:
            pass
        elif action == 2:
            if (self.game.snake.direction == Direction.UP): self.game.snake.ChangeDirection(Direction.RIGHT)
            elif (self.game.snake.direction == Direction.DOWN): self.game.snake.ChangeDirection(Direction.LEFT)
            elif (self.game.snake.direction == Direction.LEFT): self.game.snake.ChangeDirection(Direction.UP)
            elif (self.game.snake.direction == Direction.RIGHT): self.game.snake.ChangeDirection(Direction.DOWN)
        gameover = not self.game.Update()
        state = self.GetState()
        reward = 0
        if gameover: reward = -20
        if self.game.snake.checkEat: reward = 2
        return state,reward,gameover
    def Render(self):
        self.game.Draw()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption("Snake_Env")
    env = Env(40,40,20)
    state = env.Reset()
    gameover = False
    while not gameover:
        #env.game.Run()
        state,reward,gameover = env.Step(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            env.game.GetInput(event)
        env.game.Draw(screen)
        pygame.time.delay(100)