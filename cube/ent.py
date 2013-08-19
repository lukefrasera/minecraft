# Entity class to hold information about entities for 381Engine, Spring2012
# Sushil Louis

from vector import Vector3
from physics import Physics
from renderable import Renderable
from control import Control
from unitAI import UnitAI

class Entity:
    #pos  = Vector3(0, 0, 0)
    #vel  = Vector3(0, 0, 0)

    def __init__(self, engine, eid, pos = Vector3(0,0,0), mesh = 'cube.mesh', vel = Vector3(0, 0, 0), heading = 0):
        self.engine = engine
        self.eid = eid
        self.pos = pos
	self.desiredpos = Vector3(0,0,0)
        self.desiredpos.x = self.pos.x
	self.desiredpos.z = self.pos.z
        self.vel = vel
        self.mesh = mesh
        self.heading = heading
        self.speed = vel.length()
        self.commandName = "None"
        self.enode = None
	self.pitch = 0
	self.roll = 0

        self.length = 20
        self.width  = 5
        self.height = 15

        self.deltaSpeed = 5
        self.deltaYaw   = 0.01
	self.deltaTilt = 0.01

        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.acceleration  = 6
        self.turningRate   = 0.1
        self.maxSpeed = 1

        self.wakeSize = 1


        self.isSelected = False
        self.aspects = []
        self.aspectTypes = [Physics, Renderable, Control, UnitAI ]
    

        #----------------------------
        #self.initAspects()
        #----------------------------
        pass

    def initAspects(self):
        for aspectType in self.aspectTypes:
            self.aspects.append(aspectType(self))
        for aspect in self.aspects:
            aspect.initialize()

    def tick(self, dtime):
        for aspect in self.aspects:
            aspect.tick(dtime)

    def findAspect(self, aspType):
        for asp in self.aspects:
            if aspType == type(asp):
                return asp
        return None

    def __str__(self):
        x = "Entity: %s \nPos: %s, Vel: %s,  mesh = %s\nSpeed: %f, Heading: %f" % (self.uiname, str(self.pos), str(self.vel), self.mesh, self.speed, self.heading)
        return x


class CUBE(Entity):
    def __init__(self, engine, eid, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), heading = 0):
        Entity.__init__(self, engine, eid, pos = pos, vel = vel, heading = heading)
        self.mesh = 'cube.mesh'
        self.uiname = 'CVN68'
        self.acceleration = 2
        self.turningRate  = 1.5
        self.maxSpeed = 1.5
        self.vel = vel
	self.move = True
        self.rollNode = None
        self.pitchNode = None
        self.isCube = True
        self.shield = False
        self.isShield = False
        self.isHidden = False
        self.isEnd = False
        
        self.wakeSize = 3
        self.length = 300
        self.width  = 50
        self.height = 70

class ENEMY(Entity):
    def __init__(self, engine, eid, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), heading = 0):
        Entity.__init__(self, engine, eid, pos = pos, vel = vel, heading = heading)
        self.mesh = 'enemy.mesh'
        self.uiname = 'CVN68'
        self.acceleration = 0
        self.turningRate  = 4
        self.maxSpeed = 0.4
        self.vel = vel
	self.move = True
        self.isCube = False
        self.isShield = False
        self.isHidden = False
        self.isEnd = False
        
        self.wakeSize = 3
        self.length = 300
        self.width  = 50
        self.height = 70

class PLANE(Entity):
    def __init__(self, engine, eid, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), heading = 0):
        Entity.__init__(self, engine, eid, pos = pos, vel = vel, heading = heading)
        self.mesh = 'plane.mesh'
        self.uiname = 'CVN68'
        self.acceleration = 2
        self.turningRate  = 0
        self.maxSpeed = 0
        self.vel = vel
	self.move = False
        self.isCube = False
        self.isShield = False
        self.isHidden = False
        self.isEnd = False
        
        self.wakeSize = 3
        self.length = 300
        self.width  = 50
        self.height = 70

class SHIELD(Entity):
    def __init__(self, engine, eid, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), heading = 0):
        Entity.__init__(self, engine, eid, pos = pos, vel = vel, heading = heading)
        self.mesh = 'shield.mesh'
        self.uiname = 'CVN68'
        self.acceleration = 2
        self.turningRate  = 0
        self.maxSpeed = 0
        self.vel = vel
	self.move = False
        self.isCube = False
        self.isShield = True
        self.isHidden = False
        self.isEnd = False
        
        self.wakeSize = 3
        self.length = 300
        self.width  = 50
        self.height = 70

class HIDDEN(Entity):
    def __init__(self, engine, eid, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), heading = 0):
        Entity.__init__(self, engine, eid, pos = pos, vel = vel, heading = heading)
        self.mesh = 'obj.mesh'
        self.uiname = 'CVN68'
        self.acceleration = 2
        self.turningRate  = 0
        self.maxSpeed = 0
        self.vel = vel
	self.move = False
        self.isCube = False
        self.isShield = False
        self.isHidden = True
        self.isEnd = False
        
        self.wakeSize = 3
        self.length = 300
        self.width  = 50
        self.height = 70

class END(Entity):
    def __init__(self, engine, eid, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), heading = 0):
        Entity.__init__(self, engine, eid, pos = pos, vel = vel, heading = heading)
        self.mesh = 'life.mesh'
        self.uiname = 'CVN68'
        self.acceleration = 2
        self.turningRate  = 0
        self.maxSpeed = 0
        self.vel = vel
	self.move = False
        self.isCube = False
        self.isShield = False
        self.isHidden = False
        self.isEnd = True
        
        self.wakeSize = 3
        self.length = 300
        self.width  = 50
        self.height = 70

