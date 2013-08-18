# Render code for renderables
# vel is rate of change of pos
# Sushil Louis
from aspect import Aspect
from vector import Vector3
import math

class Renderable(Aspect):
    def __init__(self, ent):
        Aspect.__init__(self, ent)
        self.node = None

    def initialize(self):
        # make scenenode for entity
        if self.ent.isCube:
            print "Renderable: ", self.ent.uiname, self.ent.mesh
            e = self.ent.engine.gfxMgr.sceneManager.createEntity(self.ent.uiname + str(self.ent.eid), self.ent.mesh)
            self.ent.pitchNode = self.ent.engine.gfxMgr.sceneManager.getRootSceneNode().createChildSceneNode('cubePitchNode', self.ent.pos)
            self.ent.rollNode = self.ent.pitchNode.createChildSceneNode('cubeRollNode')
            self.node = self.ent.rollNode.createChildSceneNode('cubeNode')
            self.node.attachObject(e)
            self.ent.enode = self.node

        else:
            print "Renderable: ", self.ent.uiname, self.ent.mesh
            e = self.ent.engine.gfxMgr.sceneManager.createEntity(self.ent.uiname + str(self.ent.eid), self.ent.mesh)
            self.node = self.ent.engine.gfxMgr.sceneManager.getRootSceneNode().createChildSceneNode(self.ent.uiname + str(self.ent.eid) + '_node', self.ent.pos)
            self.node.attachObject(e)
            self.ent.enode = self.node

    def tick(self, dtime):
        if self.ent.isCube:
            # copy entity information to sceneNode
            self.ent.pitchNode.setPosition(self.ent.pos)
            self.node.yaw(self.ent.heading)
            self.ent.pitchNode.resetOrientation()
            self.ent.rollNode.resetOrientation()
            self.ent.pitchNode.pitch(self.ent.pitch)
	    self.ent.rollNode.roll( self.ent.roll)
        else:
            # copy entity information to sceneNode
            self.node.setPosition(self.ent.pos)
            self.node.resetOrientation()
            self.node.yaw(self.ent.heading)
            self.node.pitch(self.ent.pitch)
	    self.node.roll( self.ent.roll)



        #---------------------------------------------
        # decorate ent for selection
        #---------------------------------------------

        #---------------------------------------------
        # other decorations
        #---------------------------------------------

