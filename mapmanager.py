from panda3d.core import CollisionBox, CollisionNode, Vec4

class Mapmanager:
    def __init__(self):
        self.color = (0.2, 0.8, 0.2, 1)
        self.blocks = []
        
        self.startNew()
        self.createMap()
    
    def startNew(self):
        self.land = render.attachNewNode("Land")
    
    def addBlock(self, position, color=None):
        if color is None:
            color = self.color
        
        self.block = loader.loadModel("models/box")
        self.block.setPos(position)
        self.block.setScale(1)
        self.block.setColor(color[0], color[1], color[2], color[3])
        self.block.reparentTo(self.land)
        self.blocks.append(self.block)
        
        # Add collision to block
        collision_box = CollisionBox(0, 0, 0, 1, 1, 1)
        collision_node = CollisionNode(f"block_collision_{len(self.blocks)}")
        collision_node.addSolid(collision_box)
        self.block.attachNewNode(collision_node)
    
    def createMap(self):
        """Generate the game map with terrain"""
        # Ground platform (5x5 green blocks)
        for x in range(5):
            for z in range(5):
                self.addBlock((x, 10, z), (0.2, 0.8, 0.2, 1))
        
        # Stairs - ascending platform
        for i in range(4):
            for j in range(3):
                self.addBlock((6 + i, 10 + i, j), (0.5, 0.5, 0.8, 1))
        
        # Tower - stacked blocks
        for y in range(5):
            self.addBlock((10, 10 + y, 2), (0.8, 0.6, 0.2, 1))
        
        # Bridge
        for x in range(6):
            self.addBlock((10 + x, 14, 2), (0.7, 0.7, 0.7, 1))
        
        # Landing platform
        for x in range(4):
            for z in range(4):
                self.addBlock((15 + x, 14, z), (0.2, 0.8, 0.2, 1))
        
        # Obstacles - stone blocks
        for y in range(3):
            self.addBlock((17, 14 + y, -2), (0.6, 0.6, 0.6, 1))
    
    def create_collision_mesh(self):
        """Create collision geometry for terrain"""
        for block in self.blocks:
            collision_box = CollisionBox(0, 0, 0, 1, 1, 1)
            collision_node = CollisionNode(f"terrain_{id(block)}")
            collision_node.addSolid(collision_box)
            block.attachNewNode(collision_node)
