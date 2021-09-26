
class Ratio:
    def __init__(self, w, h) -> None:
        self.width = w
        self.heigth = h
    
    def getMultiplier(self, m) -> tuple:
        return (self.width * m, self.heigth * m)

    def getByWidth(self, w) -> tuple:
        multiplier = w / self.width
        return (w, multiplier * self.heigth)

    def getByHeigth(self, h) -> tuple:
        multiplier = h / self.heigth
        return (multiplier * self.width, h)