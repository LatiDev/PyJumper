import pygame as pg
import pygame.key as pgKey
import pygame.transform as pgTranf
from body import *
from input import *

IDLE_ANIMATION = 0
WALK_ANIMATION = 1
JUMP_ANIMATION = 2

class Character(Body):
    """
    Body that Moves Like a Human
    """
    def __init__(self, 
        position: tuple, 
        animationMngr: AnimationManager, 
        movementSpeed : int,
        jumpSpeed : int,
        maxJumps : int,
        type: list = [], 
        rgbCode: tuple = None):
        super().__init__(position, animationMngr, type, rgbCode)

        self.movementSpeed = movementSpeed
        self.jumpSpeed = jumpSpeed
        self.maxJumps = maxJumps
        self.currentjumps = maxJumps

        self.lastBodyCollied : list[BodyCollision] = []
        self.collisionDirection : int = 0
        self.horinDir : int = 0

        self.isOnFloor : bool = False
        self.isInAir : bool = False
        self.isJumping : bool = False

        self.inAirFrames : int = 1
        self.isAnimationFlip : int = 0
        self.lastMove : list = []

    def move(self, direction, bodys):
        left = 1 if direction & LEFT > 0 else 0
        rigth = 1 if direction & RIGTH > 0 else 0
        up = 1 if direction & UP > 0 else 0
        down = 1 if direction & DOWN > 0 else 0
        
        if (left or rigth):
            self.horinDir = rigth - left

        self.isAnimationFlip = 1 if self.horinDir == -1 else 0
        self.collisionDirection = Body.getCollisionDirection(self.lastBodyCollied)
        
        self.isOnFloor = self.collisionDirection & COLLIDING_DOWN > 0
        self.isInAir = self.collisionDirection & COLLIDING_DOWN == 0

        if self.isInAir:
            self.inAirFrames += 1
        else:
            self.inAirFrames = 1

        nextAnimation = IDLE_ANIMATION
        self.lastMove = [self.movementSpeed * (rigth - left), 1 + (self.inAirFrames / 4)]
        if rigth or left:
            nextAnimation = WALK_ANIMATION

        if self.isInAir:
            nextAnimation = JUMP_ANIMATION

        if (up and self.currentjumps > 0 and not self.isJumping):
            self.lastMove[1] = 0
            self.isJumping = True
            self.currentjumps -= 1

        if self.isJumping:
            self.lastMove[1] += -self.jumpSpeed

        #print(self.lastMove)
        #self.AddPosition(self.lastMove)
        self.lastBodyCollied = self.alt(self, self.lastMove, bodys)
        self.play(nextAnimation)

        if (self.isOnFloor):
            self.isJumping = False
            self.currentjumps = self.maxJumps

    def debugDisplay(self, displayText, color):    
        displayText("Player:", color)
        displayText(f"-Collide Number: {self.collisionDirection}", color)
        displayText(f"-in Air: {self.isInAir}", color)
        displayText(f"-Air Frames: {self.inAirFrames}", color)
        displayText(f"-Current Animation: {self.animationMngr.getCurrentAnimation()}", color)
        displayText(f"-Animations Flip: {self.isAnimationFlip}", color)
        displayText(f"-Current Jumps: {self.currentjumps}", color)
        displayText(f"-is Jumping: {self.isJumping}", color)
        displayText(f"-Velocity: {self.lastMove}", color)
        displayText(f"-Position: {self.getPosition()}", color)
        displayText(f"-Gravity: {1 + self.inAirFrames / 4}", color)
        displayText(f"-Jump Speed: {-self.jumpSpeed}", color)
        displayText(f"-is On Floor: {self.isOnFloor}", color)
