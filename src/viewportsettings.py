
class ViewportSettings:
    def __init__(self, 
        size : tuple, 
        flags : int,
        vsync : int) -> None:
        
        self.size = size
        self.flags = flags
        self.vsync = vsync