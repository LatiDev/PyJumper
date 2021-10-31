from Component import *

class GameObject:
    __ALL : list['GameObject'] = []
    def __init__(self, 
    components : list[Component], 
    #childs : list['GameObject'] = []
    ):
        self.__components = components
        """
        self.__childs : list = childs
        """
        GameObject.__ALL.append(self)

    def __findComponent(self, type : type) -> Component:
        for component in self.__components:
            if (isinstance(component, type)):
                return component
        raise Exception(f"Couldn't find component {type} in gameobject")

    def getComponent(self, type):
        if (issubclass(type, Component)):
            return self.__findComponent(type)
        raise Exception(f"type {type} is not subclass of component")

    """
    def getChild(self, index : int):
        if (index >= 0 and index < len(self.__childs)):
            return self.__childs[index]
        else:
            raise Exception(f"index {index} out of bound")
    """

    def addComponent(self, component):
        if (issubclass(component, Component)):
            self.__components.append(component)
        else:
            raise Exception(f"type {component} is not subclass of component")

    """
    def addChild(self, child : 'GameObject'):
        self.__childs.append(child)
    """

    def removeComponent(self, index : int):
        if (index >= 0 and index < len(self.__components)):
            self.__components.pop(index)
        else:
            raise Exception(f"index {index} out of bound")

    """
    def removeChild(self, index : int):
        if (index >= 0 and index <  len(self.__childs)):
            self.__childs.pop(index)
        else:
            raise Exception(f"index {index} out of bound")
    """