from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.land = mapmanager()
        base.camLens.setFov(90)
base = Game()
base.run()