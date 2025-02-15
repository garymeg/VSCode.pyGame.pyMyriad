import pygame
import settings
import element
import random

class ReflectedBullet(element.Element):
    def __init__(self,game,x,y,wave):

        bulletSet = "CEG"[game.powerUp]

        imgDir = 'Lasers/Set' + bulletSet
        super().__init__(game,x,y,imgDir)

        self.imDead = False

        image = super().loadAnimationFrame(f'Laser{bulletSet}',wave - 1, 270, 0.25)
        self.animation.append(image)

        image = pygame.transform.flip(image,True,False)
        self.animation.append(image)

        super().setAnimationFrame(self.animation[0],True)

        self.noOfFrames = 2
        self.speed = 24

        self.ticksPerFrame = settings.FRAMES_PER_SECOND / 4
        self.reflective = False
        self.myValue = 0

    def update(self):
        super().move(0,1,self.speed-1,False)
        #self.Y -=24

        self.tickCounter += 1
        if self.tickCounter >= settings.FRAMES_PER_SECOND:
            self.tickCounter = 0

        frameNo = int(self.tickCounter // self.ticksPerFrame)
        frameNo = frameNo % 2

        super().setAnimationFrame(self.animation[frameNo],True)

        if self.Y > settings.Screen.HEIGHT + self.rect.height:
            self.imDead = True
        else:
            self.rect.centerx = self.X
            self.rect.centery = self.Y


