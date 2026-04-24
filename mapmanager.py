class Mapmanager:
    def __init__(self):
        self.startNew()
        self.createMap()

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def addBlock(self, position, color):
        block = loader.loadModel("models/box")
        block.setPos(position)
        block.setScale(1)
        block.setColor(color)
        block.reparentTo(self.land)

    def createMap(self):
        size = 8

        for x in range(size):
            for y in range(size):
                if x == 0 or y == 0 or x == size - 1 or y == size - 1:
                    color = (0.5, 0.5, 0.5, 1)
                    z = 1
                elif (x + y) % 2 == 0:
                    color = (0.2, 0.8, 0.2, 1)
                    z = 0
                else:
                    color = (0.2, 0.4, 0.9, 1)
                    z = 0

                self.addBlock((x, y + 10, z), color)
