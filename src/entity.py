
class Entity:
    ALL : list = []
    def __init__(self):
        Entity.ALL.append(self)
    
    def allStart():
        for entity in Entity.ALL:
            entity.onStart()
    
    def allUpdate(delta : float):
        for entity in Entity.ALL:
            entity.onUpdate(delta)
    
    def onStart(self):
        pass
    
    def onUpdate(self, delta : float):
        pass