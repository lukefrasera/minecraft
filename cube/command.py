import utils
from vector import Vector3
import math

class Target(object):
    
    def __init__(self, ent, location):
        self.ent = ent
        self.location = location


class Command(object):
    MOVEDISTANCETHRESHOLD = 10000
    def __init__(self, ent, target):
        self.ent    = ent
        self.target = target
        self.name   = None
        self.ent.commandName = "None"
        threshold = self.ent.length * 5
        self.MOVEDISTANCETHRESHOLD = threshold*threshold

    def done(self):
        return False

    def init(self):
        pass

    def tick(self, dt):
        pass

import math
class Move(Command):
    def __init__(self, ent, target):
        Command.__init__(self, ent, target)
        self.ent.commandName = "Move"
        self.name = "Move"
        
    def init(self):
        diff = self.target.location - self.ent.pos
        self.ent.desiredHeading = utils.fixAngle(- math.atan2(diff.z, diff.x))
        self.ent.desiredSpeed   = self.ent.maxSpeed
        

    def done(self):
        return self.ent.pos.squaredDistance(self.target.location) < self.MOVEDISTANCETHRESHOLD

    def tick(self, dt):
        squaredDistance = self.target.location.squaredDistance(self.ent.pos)
        if squaredDistance < self.MOVEDISTANCETHRESHOLD: 
            self.ent.desiredSpeed = 0



        
class Ram(Command):
    def __init__(self, ent, target):
        Command.__init__(self, ent, target)
        self.ent.commandName = "Ram"
        self.name = "Ram"

        print self.ent.uiname, " will ram ", self.target.ent.uiname
        pass

    def init(self):
        self.ent.desiredSpeed   = self.ent.maxSpeed

    def done(self):
        return self.ent.pos.squaredDistance(self.target.ent.pos) < self.ent.length

    def tick(self, dt):
        diff = self.target.ent.pos - self.ent.pos
        relativeVel = self.target.ent.vel - self.ent.vel
        timeToClose = diff.length()/(relativeVel.length() + 1)
        aimLocation = self.target.ent.pos + self.target.ent.vel * timeToClose
        diff = aimLocation - self.ent.pos
        self.ent.desiredHeading = utils.fixAngle(- math.atan2(diff.z, diff.x))
        if self.done():
            self.ent.desiredSpeed = 0
        else:
            self.ent.desiredSpeed   = self.ent.maxSpeed        
        

        
