from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.land = Mapmanager()

        base.camera.setPos(4, -10, 10)
        base.camera.setHpr(0, -35, 0)
        base.camLens.setFov(90)

game = Game()
game.run()
