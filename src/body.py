import pygame as pg
import pygame.rect as pgRect
from sprite import *
from bodycollision import *

COLLIDING_UP    = 8
COLLIDING_DOWN  = 4
COLLIDING_LEFT  = 2
COLLIDING_RIGHT = 1

class Body(Sprite):
    """
    Sprite that can collide with others Bodys
    """
    def __init__(self, 
        position: tuple, 
        animationMngr: AnimationManager, 
        type: list, 
        rgbCode: tuple):
        super().__init__(position, animationMngr, type, [], rgbCode)

    def isColliding(self, body):
        return self.rect.colliderect(body.rect)

    def getCollisionDirection(bodysCollisions : list[BodyCollision]) -> int:
        collisionDirection : int = 0
        for bodyCollision in bodysCollisions:
            collisionDirection |= bodyCollision.nbCollision
        return collisionDirection

    def fixCollision(self, body):
        bodyCollied : list[Body] = []
        nbCollision : int = 0

        position = self.getPosition()
        if self.isColliding(body):
            if position[0] > 0:
                self.rect.right = body.rect.left
                nbCollision += COLLIDING_RIGHT
            elif position[0] < 0:
                self.rect.left = body.rect.right
                nbCollision += COLLIDING_LEFT
            bodyCollied.append(body)

        if self.isColliding(body):
            if position[1] > 0:
                self.rect.bottom = body.rect.top
                nbCollision += COLLIDING_DOWN
            elif position[1] < 0:
                self.rect.top = body.rect.bottom 
                nbCollision += COLLIDING_UP
            bodyCollied.append(body)

        return BodyCollision(bodyCollied, nbCollision)

    def fixCollisions(self, bodys : list) -> list[BodyCollision]:
        bodysCollied : list[BodyCollision] = []
        for body in bodys:
            bodysCollied.append(self.fixCollision(body))
        return bodysCollied

    def getIndexBody(self, list, value, nbCollision):
        index : int = -1
        for item in range(len(list)):
            if (list[item].body == value):
                index = item
        return index

    def alt(self, body, position : tuple, bodys : list):
        bodyCollied : list[BodyCollision] = []
        nbCollision : int = 0

        body.rect.x += position[0]
        for b in bodys:   
            if body.rect.colliderect(b):
                if position[0] > 0:
                    body.rect.right = b.left
                    #nbCollision += COLLIDING_RIGHT
                elif position[0] < 0:
                    body.rect.left = b.right
                    #nbCollision += COLLIDING_LEFT
                #bodyCollied.append(BodyCollision(b, nbCollision))

        body.rect.y += position[1]
        for b in bodys:
            if body.rect.colliderect(b):
                #indexBody : int = self.getIndexBody(bodys, b, nbCollision)
                if position[1] > 0:
                    body.rect.bottom = b.top
                    #if (indexBody > -1):
                    #    bodyCollied[indexBody].nbCollision |= COLLIDING_DOWN
                    #else:
                    #    bodyCollied.append(BodyCollision(b, nbCollision))
                
                elif position[1] < 0:
                    body.rect.top = b.bottom 
                    #if (indexBody > -1):
                    #    bodyCollied[indexBody].nbCollision |= COLLIDING_UP
                    #else:
                    #    bodyCollied.append(BodyCollision(b, nbCollision))

        return bodyCollied