# Simple ORIENTED Physics for 38Engine
# vel is rate of change of pos
# Sushil Louis

from vector import Vector3
from aspect import Aspect
import utils
import math
import ogre.renderer.OGRE as ogre


class Physics (Aspect):
    def __init__(self, ent):
        Aspect.__init__(self, ent)
        pass 
        
    def tick(self, dtime):
        #----------position-----------------------------------
        if self.ent.move:
	    if (self.ent.desiredpos.x - self.ent.pos.x) > 0:
	         self.ent.pos.x += dtime * self.ent.maxSpeed
		 self.ent.roll -= (math.pi/2) * dtime * self.ent.turningRate
	    if (self.ent.desiredpos.x - self.ent.pos.x) < 0:
	         self.ent.pos.x -= dtime * self.ent.maxSpeed
		 self.ent.roll += (math.pi/2) * dtime * self.ent.turningRate
	    if (self.ent.desiredpos.z - self.ent.pos.z) > 0:
	         self.ent.pos.z += dtime * self.ent.maxSpeed
		 self.ent.pitch += (math.pi/2) * dtime * self.ent.turningRate
	    if (self.ent.desiredpos.z - self.ent.pos.z) < 0:
	         self.ent.pos.z -= dtime * self.ent.maxSpeed
		 self.ent.pitch -= (math.pi/2) * dtime * self.ent.turningRate
            if self.ent.isCube:
	        if self.ent.pos.x < self.ent.desiredpos.x + 0.02 and self.ent.pos.x > self.ent.desiredpos.x - 0.02:
	            self.ent.pos.x = self.ent.desiredpos.x
	        if self.ent.pos.z < self.ent.desiredpos.z + 0.02 and self.ent.pos.z > self.ent.desiredpos.z - 0.02:
	            self.ent.pos.z = self.ent.desiredpos.z

            if self.ent.pitch > -math.pi/2 - 0.02 and self.ent.pitch < -math.pi/2 + 0.02:
		self.ent.pitch = 0.0
		self.ent.roll = 0.0
            if self.ent.pitch > math.pi/2 - 0.02 and self.ent.pitch < math.pi/2 + 0.02:
		self.ent.pitch = 0.0
		self.ent.roll = 0.0


            if self.ent.roll > -math.pi/2 - 0.02 and self.ent.roll < -math.pi/2 + 0.02:
		self.ent.roll = 0.0
		self.ent.pitch = 0.0
            if self.ent.pitch > math.pi/2 - 0.02 and self.ent.roll < math.pi/2 + 0.02:
		self.ent.roll = 0.0
		self.ent.pitch = 0.0


