
class Event:
    def __init__(self, func, order):
        self.func = func
        self.order = order

class EventDivuser:
    def __init__(self, critera):
        self.events : list[Event] = []
        self.critera = critera
    
    def add(self, event : Event):
        self.events.append(event)

    def end(self):
        self.events.sort(key=self.critera)

    def diffuse(self, value):
        for event in self.events:
            event.func(value)