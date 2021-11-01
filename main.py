import pygame
import time
import windowFramework


#class layout (time, damage, towers...)
#class heroes
#class level

class level_frame:
    def __init__(self, width, height, window):
        self.width, self.height = width, height
        self.window = window
        self.map1 = pygame.image.load("map/lvl1.jpg")
        self.map1 = pygame.transform.scale(self.map1, (self.width, self.height))

    def draw(self):
        self.window.blit(self.map1, (0, 0))

class heroes_frame:
    def __init__(self, width, height, window):
        self.width, self.height = width, height
        self.window = window
        self.xInicial, self.yInicial = 10, self.height/2
        self.x, self.y = self.xInicial, self.yInicial

        self.ninjaIdleRight = [pygame.image.load("ninja/idle1.png"), pygame.image.load("ninja/idle1.png"), pygame.image.load("ninja/idle1.png"), pygame.image.load("ninja/idle2.png"), pygame.image.load("ninja/idle2.png"), pygame.image.load("ninja/idle2.png"), pygame.image.load("ninja/idle3.png"), pygame.image.load("ninja/idle3.png"), pygame.image.load("ninja/idle3.png"), pygame.image.load("ninja/idle2.png"), pygame.image.load("ninja/idle2.png"), pygame.image.load("ninja/idle2.png"), pygame.image.load("ninja/idle1.png"), pygame.image.load("ninja/idle1.png"), pygame.image.load("ninja/idle1.png")]

        self.ninjaIdleLeft = [pygame.image.load("ninja/idle1flop.png"), pygame.image.load("ninja/idle1flop.png"), pygame.image.load("ninja/idle1flop.png"), pygame.image.load("ninja/idle2flop.png"), pygame.image.load("ninja/idle2flop.png"), pygame.image.load("ninja/idle2flop.png"), pygame.image.load("ninja/idle3flop.png"), pygame.image.load("ninja/idle3flop.png"), pygame.image.load("ninja/idle3flop.png"), pygame.image.load("ninja/idle2flop.png"), pygame.image.load("ninja/idle2flop.png"), pygame.image.load("ninja/idle2flop.png"), pygame.image.load("ninja/idle1flop.png"), pygame.image.load("ninja/idle1flop.png"), pygame.image.load("ninja/idle1flop.png")]

        self.ninjaWalk = [pygame.image.load("ninja/walk1.png"), pygame.image.load("ninja/walk1.png"), pygame.image.load("ninja/walk2.png"), pygame.image.load("ninja/walk2.png"), pygame.image.load("ninja/walk3.png"), pygame.image.load("ninja/walk4.png"), pygame.image.load("ninja/walk4.png"), pygame.image.load("ninja/walk5.png"), pygame.image.load("ninja/walk5.png"), pygame.image.load("ninja/walk4.png"), pygame.image.load("ninja/walk4.png"), pygame.image.load("ninja/walk3.png"), pygame.image.load("ninja/walk2.png"), pygame.image.load("ninja/walk2.png"), pygame.image.load("ninja/walk1.png")]

        self.ninjaWalkFlop = [pygame.image.load("ninja/walk1flop.png"), pygame.image.load("ninja/walk1flop.png"), pygame.image.load("ninja/walk2flop.png"), pygame.image.load("ninja/walk2flop.png"), pygame.image.load("ninja/walk3flop.png"), pygame.image.load("ninja/walk4flop.png"), pygame.image.load("ninja/walk4flop.png"), pygame.image.load("ninja/walk5flop.png"), pygame.image.load("ninja/walk5flop.png"), pygame.image.load("ninja/walk4flop.png"), pygame.image.load("ninja/walk4flop.png"), pygame.image.load("ninja/walk3flop.png"), pygame.image.load("ninja/walk2flop.png"), pygame.image.load("ninja/walk2flop.png"), pygame.image.load("ninja/walk1flop.png")]

        self.count = 0
        self.walkRight = False
        self.walkLeft = False
        self.idleRight = True
        self.idleLeft = False 
        self.jumping = False
        self.canJump = False

    def movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d] and not(key[pygame.K_a]) and (self.x < self.width - 130):
            self.x += 5
            self.idleRight = False
            self.idleLeft = False
            self.walkRight = True

        else:
            if not(self.walkLeft) and self.walkRight:
                self.idleRight = True
            self.walkRight = False

        if key[pygame.K_a] and not(key[pygame.K_d]) and (self.x >= 0):
            self.x -= 5
            self.idleRight = False
            self.idleLeft = False
            self.walkLeft = True

        else:
            if not (self.walkRight) and self.walkLeft :
                self.idleRight = False
                self.idleLeft = True 
                self.walkLeft = False
        
        if key[pygame.K_SPACE] and self.canJump: 
            self.y -= 40

        
        if self.y <= self.yInicial - 80:
            self.canJump = False

        if not(self.canJump):
            self.y += 5
               
        
        if self.y >= self.yInicial:
            self.y = self.yInicial
            self.canJump = True
    
        print(self.x, self.width, self.y, self.yInicial)


    def draw(self):
        if self.count == 12:
            self.count = 0

        else:
            if self.idleRight:
                self.window.blit(self.ninjaIdleRight[self.count], (self.x, self.y))
                self.count += 1

            if self.idleLeft:
                self.window.blit(self.ninjaIdleLeft[self.count], (self.x, self.y))
                self.count += 1

            if self.walkRight:
                self.window.blit(self.ninjaWalk[self.count], (self.x, self.y))
                self.count += 1

            if self.walkLeft:
                self.window.blit(self.ninjaWalkFlop[self.count], (self.x, self.y))
                self.count += 1

        


window = windowFramework.window()
level = level_frame(window.width, window.height, window.window)
heroes = heroes_frame(window.width, window.height, window.window)

relog = pygame.time.Clock()
while not window.endFrame():
    level.draw()
    heroes.draw()
    heroes.movement()
    window.updateFrame()

    relog.tick(30)
