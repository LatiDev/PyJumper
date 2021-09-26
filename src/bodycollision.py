class BodyCollision():
    def __init__(self, 
        body, 
        nbCollision : int):
        
        self.body = body
        self.nbCollision = nbCollision

    def isCollisionOn(self, direction : int) -> bool:
        return self.nbCollision & direction > 0