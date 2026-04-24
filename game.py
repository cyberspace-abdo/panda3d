from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from mapmanager import Mapmanager
from panda3d.core import Vec3, CollisionTraverser, CollisionHandlerPusher, CollisionSphere, CollisionNode
from direct.gui.OnscreenText import OnscreenText
import math

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Game settings
        self.player_speed = 50
        self.jump_power = 25
        self.gravity = -32.2
        
        # Player state
        self.player_vel_y = 0
        self.on_ground = False
        
        # Input handling
        self.keys = {'w': False, 'a': False, 's': False, 'd': False, 'space': False}
        
        # Setup game
        self.setup_lighting()
        self.land = Mapmanager()
        self.setup_collisions()
        self.setup_player()
        self.setup_camera()
        self.setup_input()
        self.setup_hud()
        
        # Game loop
        self.taskMgr.add(self.update_game, "UpdateGame")
    
    def setup_lighting(self):
        """Setup ambient and directional lighting"""
        from panda3d.core import AmbientLight, DirectionalLight, Vec4
        
        ambient_light = AmbientLight("ambient")
        ambient_light.setColor(Vec4(0.6, 0.6, 0.6, 1))
        ambient_np = self.render.attachNewNode(ambient_light)
        self.render.setLight(ambient_np)
        
        dir_light = DirectionalLight("directional")
        dir_light.setColor(Vec4(0.8, 0.8, 0.8, 1))
        dir_light_np = self.render.attachNewNode(dir_light)
        dir_light_np.setHpr(45, -60, 0)
        self.render.setLight(dir_light_np)
    
    def setup_collisions(self):
        """Setup collision system"""
        self.cTrav = CollisionTraverser()
        self.player_handler = CollisionHandlerPusher()
        self.player_handler.setHorizontal(False)
    
    def setup_player(self):
        """Create player character"""
        self.player = self.loader.loadModel("models/box")
        self.player.setPos(2, 11.5, 2)
        self.player.setScale(0.5, 1.5, 0.5)
        self.player.setColor(1, 0, 0, 1)
        self.player.reparentTo(self.render)
        
        # Player collision
        collision_sphere = CollisionSphere(0, 0, 0, 0.7)
        collision_node = CollisionNode("player_collision")
        collision_node.addSolid(collision_sphere)
        self.player_collision = self.player.attachNewNode(collision_node)
        self.cTrav.addCollider(self.player_collision, self.player_handler)
        
        self.player_pos = Vec3(2, 11.5, 2)
    
    def setup_camera(self):
        """Setup camera"""
        base.camLens.setFov(90)
    
    def setup_input(self):
        """Setup keyboard input"""
        for key in ['w', 'a', 's', 'd']:
            self.accept(key, self.set_key, [key, True])
            self.accept(f"{key}-up", self.set_key, [key, False])
        
        self.accept("space", self.set_key, ["space", True])
        self.accept("space-up", self.set_key, ["space", False])
    
    def set_key(self, key, value):
        """Track key state"""
        self.keys[key] = value
    
    def update_game(self, task):
        """Main game update loop"""
        dt = globalClock.getDt()
        
        self.update_player(dt)
        self.update_camera()
        self.cTrav.traverse(self.render)
        
        return Task.cont
    
    def update_player(self, dt):
        """Update player position and physics"""
        movement = Vec3(0, 0, 0)
        
        # Horizontal movement
        if self.keys['w']:
            movement.z -= self.player_speed * dt
        if self.keys['s']:
            movement.z += self.player_speed * dt
        if self.keys['a']:
            movement.x -= self.player_speed * dt
        if self.keys['d']:
            movement.x += self.player_speed * dt
        
        # Apply movement
        self.player.setX(self.player.getX() + movement.x)
        self.player.setZ(self.player.getZ() + movement.z)
        
        # Gravity and jumping
        self.player_vel_y += self.gravity * dt
        self.player.setY(self.player.getY() + self.player_vel_y * dt)
        
        # Ground collision
        if self.player.getY() <= 11.5:
            self.player.setY(11.5)
            self.player_vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False
        
        # Jumping
        if self.keys['space'] and self.on_ground:
            self.player_vel_y = self.jump_power
            self.on_ground = False
            self.keys['space'] = False
        
        self.player_pos = self.player.getPos()
    
    def update_camera(self):
        """Update camera to follow player"""
        camera_height = 8
        camera_distance = 15
        
        cam_x = self.player_pos.x - math.sin(math.radians(45)) * camera_distance
        cam_z = self.player_pos.z + math.cos(math.radians(45)) * camera_distance
        cam_y = self.player_pos.y + camera_height
        
        self.camera.setPos(cam_x, cam_y, cam_z)
        self.camera.lookAt(self.player_pos.x, self.player_pos.y + 2, self.player_pos.z)
    
    def setup_hud(self):
        """Setup heads-up display"""
        OnscreenText(text="PANDA3D 3D PLATFORMER", pos=(0, 0.9), scale=0.08, fg=(1, 1, 1, 1))
        OnscreenText(text="[W/A/S/D] Move | [SPACE] Jump", pos=(0, -0.9), scale=0.05, fg=(1, 1, 1, 1))


if __name__ == "__main__":
    game = Game()
    game.run()
