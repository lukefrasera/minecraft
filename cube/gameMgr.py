from vector import Vector3
from mgr import Mgr
import ogre.renderer.OGRE as ogre
import math


class GameMgr (Mgr):
    def __init__(self, engine):
        Mgr.__init__(self, engine)
	self.invalid = []
        self.enemies = []
        self.items = []
        self.points = 500
        self.time = 0
        self.hidden = 0
        self.lives = 2
        self.win = False
        print "starting Game mgr"

        pass

    def loadLevel(self):
        self.game1()

    def tick(self, dtime):
        if not self.win:
            self.time+= dtime
            self.points-= dtime*2
	    for item in self.items:
                item.desiredpos = self.player.pos
                dist = item.pos.squaredDistance( self.player.pos )
                if dist <= 0.8:
                    if item.isShield:
                        self.player.shield = True
                        self.points+=10
                        item.pos = Vector3(0,-10,0)
                    if item.isHidden:
                        self.hidden+=1
                        self.points+=200
                        item.pos = Vector3(0,-10,0)
                    if item.isEnd:
                        self.win = True
                        self.player.move = False
                        for ent in self.enemies:
                            ent.move = False

	    for ent in self.enemies:
                ent.desiredpos = self.player.pos
                dist = ent.pos.squaredDistance( self.player.pos )
                if dist <= 1.0:
                    if self.player.shield:
                        self.player.shield = False
                        ent.move = False
                        ent.pos = Vector3(0,-10,0)
                    else:
                        self.player.pos = Vector3(0,0.5,0)
                        self.player.desiredpos = Vector3(0,0.5,0)
                        self.player.pitch = 0
                        self.player.roll = 0
                        self.lives-=1
                        self.points-=200
                        ent.move = False
                        ent.pos = Vector3(0,-10,0)

            if self.lives <= 0:
                self.player.move = False
            self.engine.gfxMgr.camYawNode.position = Vector3(self.player.pos.x, 8, self.player.pos.z)
        
        

    def game1(self):
        enemy = self.engine.entMgr.createEnt( self.engine.entMgr.entTypes[1], pos = Vector3(0,0.5,-6))
        self.enemies.append( enemy )
        enemy = self.engine.entMgr.createEnt( self.engine.entMgr.entTypes[1], pos = Vector3(8,0.5,-25))
        self.enemies.append( enemy )
        enemy = self.engine.entMgr.createEnt( self.engine.entMgr.entTypes[1], pos = Vector3(5,0.5,12))
        self.enemies.append( enemy )
        enemy = self.engine.entMgr.createEnt( self.engine.entMgr.entTypes[1], pos = Vector3(28,0.5,-20))
        self.enemies.append( enemy )
        shield = self.engine.entMgr.createEnt( self.engine.entMgr.entTypes[3], pos = Vector3(9,0.5,-3))
        shield.enode.scale(0.2,0.2,0.2)
        self.items.append( shield)
        shield = self.engine.entMgr.createEnt( self.engine.entMgr.entTypes[3], pos = Vector3(0,0.5,-2))
        shield.enode.scale(0.2,0.2,0.2)
        self.items.append( shield)
        hidden = self.engine.entMgr.createEnt( self.engine.entMgr.entTypes[4], pos = Vector3(26,0.5,-17))
        hidden.enode.scale(0.2,0.2,0.2)
        self.items.append(hidden)
        hidden = self.engine.entMgr.createEnt( self.engine.entMgr.entTypes[4], pos = Vector3(-2,0.5,15))
        hidden.enode.scale(0.2,0.2,0.2)
        self.items.append(hidden)
        hidden = self.engine.entMgr.createEnt( self.engine.entMgr.entTypes[4], pos = Vector3(-12,0.5,-10))
        hidden.enode.scale(0.2,0.2,0.2)
        self.items.append(hidden)
        hidden = self.engine.entMgr.createEnt( self.engine.entMgr.entTypes[4], pos = Vector3(6,0.5,-26))
        hidden.enode.scale(0.2,0.2,0.2)
        self.items.append(hidden)
        hidden = self.engine.entMgr.createEnt( self.engine.entMgr.entTypes[4], pos = Vector3(17,0.5,5))
        hidden.enode.scale(0.2,0.2,0.2)
        self.items.append(hidden)
        end = self.engine.entMgr.createEnt( self.engine.entMgr.entTypes[5], pos = Vector3(26,0.5,3))
        end.enode.scale(0.5,0.5,0.5)
        self.items.append(end)
        for i in range(-1,1):
            self.wall( pos = Vector3(-1,0.5,i), vert = True)
        for i in range(-1,1):
            self.wall( pos = Vector3(1,0.5,i), vert = True)
	self.wall( pos = Vector3(0,0.5,1), vert = False)
        for i in range(-5,2):
	    self.wall( pos = Vector3(i,0.5,-4), vert = False)
	for i in range(2,4):
	    self.wall( pos = Vector3(i,0.5,-2), vert = False)
	for i in range(-3,-1):
	    self.wall( pos = Vector3(i,0.5,-2), vert = False)
	for i in range(-8,-4):
            self.wall( pos = Vector3(2,0.5,i), vert = True)
	for i in range(-8,-2):
            self.wall( pos = Vector3(4,0.5,i), vert = True)
	for i in range(-3,6):
            self.wall( pos = Vector3(-6,0.5,i), vert = True)
	for i in range(-1,4):
            self.wall( pos = Vector3(-4,0.5,i), vert = True)
	for i in range(-5,4):
            self.wall( pos = Vector3(i,0.5,6), vert = False)
	for i in range(-3,8):
            self.wall( pos = Vector3(i,0.5,4), vert = False)
	for i in range(7,14):
            self.wall( pos = Vector3(4,0.5,i), vert = True)
	for i in range(-2,4):
            self.wall( pos = Vector3(i,0.5,14), vert = False)
	for i in range(-2,6):
            self.wall( pos = Vector3(i,0.5,16), vert = False)
        self.wall( pos = Vector3(-3,0.5,15), vert = True )
	for i in range(7,16):
            self.wall( pos = Vector3(6,0.5,i), vert = True)
	for i in range(7,18):
            self.wall( pos = Vector3(i,0.5,6), vert = False)
	for i in range(11,16):
            self.wall( pos = Vector3(i,0.5,4), vert = False)
	for i in range(-8,6):
            self.wall( pos = Vector3(18,0.5,i), vert = True)
	for i in range(-11,4):
            self.wall( pos = Vector3(16,0.5,i), vert = True)
	for i in range(-8,4):
            self.wall( pos = Vector3(8,0.5,i), vert = True)
	for i in range(19,25):
            self.wall( pos = Vector3(i,0.5,-9), vert = False)
	for i in range(19,25):
            self.wall( pos = Vector3(i,0.5,-11), vert = False)
	for i in range(-17,4):
            self.wall( pos = Vector3(27,0.5,i), vert = True)
	for i in range(-17,-11):
            self.wall( pos = Vector3(25,0.5,i), vert = True)
        self.wall( pos = Vector3(26,0.5,-18), vert = False)
	for i in range(-8,4):
            self.wall( pos = Vector3(25,0.5,i), vert = True)
	for i in range(-8,4):
            self.wall( pos = Vector3(8,0.5,i), vert = True)
	for i in range(-8,4):
            self.wall( pos = Vector3(10,0.5,i), vert = True)
	for i in range(5,8):
            self.wall( pos = Vector3(i,0.5,-9), vert = False)
	for i in range(0,11):
            self.wall( pos = Vector3(i,0.5,-11), vert = False)
	for i in range(11,13):
            self.wall( pos = Vector3(i,0.5,-9), vert = False)
	for i in range(-16,-9):
            self.wall( pos = Vector3(13,0.5,i), vert = True)
	for i in range(-16,-11):
            self.wall( pos = Vector3(11,0.5,i), vert = True)
	for i in range(14,16):
            self.wall( pos = Vector3(i,0.5,-17), vert = False)
	for i in range(-16,-11):
            self.wall( pos = Vector3(16,0.5,i), vert = True)
	#self.wall( pos = Vector3(17,0.5,-11), vert = False)
	for i in range(-18,-11):
            self.wall( pos = Vector3(18,0.5,i), vert = True)
	for i in range(-12,2):
            self.wall( pos = Vector3(i,0.5,-9), vert = False)
        self.wall( pos = Vector3(-13,0.5,-10), vert = True)
	for i in range(-12,-3):
            self.wall( pos = Vector3(i,0.5,-11), vert = False)
	for i in range(-18,-11):
            self.wall( pos = Vector3(-3,0.5,i), vert = True)
	for i in range(-16,-11):
            self.wall( pos = Vector3(-1,0.5,i), vert = True)
	for i in range(-2,5):
            self.wall( pos = Vector3(i,0.5,-19), vert = False)
	for i in range(0,11):
            self.wall( pos = Vector3(i,0.5,-17), vert = False)
	for i in range(8,18):
            self.wall( pos = Vector3(i,0.5,-19), vert = False)
	for i in range(-26,-19):
            self.wall( pos = Vector3(5,0.5,i), vert = True)
	for i in range(-26,-19):
            self.wall( pos = Vector3(7,0.5,i), vert = True)
        self.wall( pos = Vector3(6,0.5,-27), vert = False)
 
        self.player = self.engine.entMgr.createEnt(self.engine.entMgr.entTypes[0], pos = Vector3(0,0.5,0) )


    def wall( self, pos = Vector3(0,0,0), vert = True ):
        vect = pos
        if vert:
	    ent = self.engine.entMgr.createEnt(self.engine.entMgr.entTypes[2], pos = pos, heading = (math.pi/2))
	    self.invalid.append( ent.pos )
        if not vert:
	    ent = self.engine.entMgr.createEnt(self.engine.entMgr.entTypes[2], pos = pos, heading = 0)
	    self.invalid.append( ent.pos )



