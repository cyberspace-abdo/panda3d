from direct.showbase.ShowBase import ShowBase

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.model = loader.loadModel("models/environment")
        self.model.reparentTo(render)
        self.model.setScale(0.25, 0.25, 0.25)
        self.model.setPos(-8, 42, 0)
        base.camera.setPos(0, -20, 3)
base = ShowBase()
base.run()