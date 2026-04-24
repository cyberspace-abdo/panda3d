from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.land = Mapmanager()

        base.camera.setPos(4, -10, 10)
        base.camera.setHpr(0, -35, 0)
        base.camLens.setFov(90)

        self.accept("c", self.clearMap)
        self.accept("r", self.resetMap)
    def clearMap(self):
        self.map.clear()
    def resetMap(self):
        self.map.clear()
        self.map.createMap()

game = Game()
game.run()
