import ogre.io.OIS as OIS

from aspect import Aspect
import utils

class Control(Aspect):
    def __init__(self, ent):
        Aspect.__init__(self, ent)

    def initialize(self):
        self.ent.desiredHeading = 0
        self.ent.desiredSpeed = 0
        self.keyboard = self.ent.engine.inputMgr.keyboard
        self.toggle = 0.15
        


    def tick(self, dtime):
        self.keyboard.capture()
        if self.toggle >= 0: 
           self.toggle -= dtime



