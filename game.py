import pygame
from pygame.locals import *
import time
import random

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resource/apple.jpg")
        self.x = 40*10
        self.y = 40*10

    def draw(self):
        self.parent_screen.blit(self.image,(self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*40
        self.y = random.randint(1,19)*40
    
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))     #self.surface becomes an object of set_mode method.
        #creating an object self.snake of class snake().
        self.snake = snake(self.surface, 2)
        self.snake.draw()
        #creating an object self.apple of class Apple().
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()
        
        for i in range(self.snake.length):
        #we just have to check whether the snake head collides with apple co ordinates          
            if self.is_collision(self.snake.x[i], self.snake.y[i],self.apple.x, self.apple.y):
                #increase length after collison.
                self.snake.increase_length()
                #move apple after collision
                self.apple.move()
            

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + 40:
            if y1 >= y2 and y1 <= y2 + 40:
                return True
        return False

    def run(self):
        
        running = True
    
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        pygame.quit()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()
                        

                    
                elif event.type == QUIT:
                    running = False
                    pygame.quit()

            self.play()
            time.sleep(0.3)

class snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resource/block.jpg")
        self.length = length
        self.x = [40]*length
        self.y = [40]*length
        self.direction = 'down'

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill((52,235,195))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'
        
    def move_left(self):
        self.direction = 'left'
        
    def move_right(self):
        self.direction = 'right'

    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        '''
        size of lock is 40x40 pixels
        that is why move block by 40 pix
        '''
        if self.direction == 'left':
            self.x[0] -= 40    

        elif self.direction == 'right':
            self.x[0] += 40

        elif self.direction == 'up':
            self.y[0] -= 40

        elif self.direction == 'down':
            self.y[0] += 40
        self.draw()
        

    
if __name__=='__main__':

    game = Game()
    game.run()
    


    
                
               
