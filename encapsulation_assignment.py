class Protected:
    def __init__(self):
        self._protectedVar = 0
        self.__privateVar = 8

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj._protectedVar = 16
obj.getPrivate()
obj.setPrivate(31)
obj.getPrivate()

print(obj._protectedVar)
