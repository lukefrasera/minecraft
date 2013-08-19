from vector import Vector3
from mgr import Mgr



class EntMgr (Mgr):
    def __init__(self, engine):
        Mgr.__init__(self, engine)
        print "starting ent mgr"

        self.ents = {}
        self.nEnts = 0
        self.selectedEntIndex = 0
        self.selectedEnt = None
        import ent
        self.entTypes = [ent.CUBE, ent.ENEMY, ent.PLANE, ent.SHIELD, ent.HIDDEN, ent.END]
        

    def createEnt(self, entType, pos = Vector3(0,0,0), heading = 0):
        ent = entType(self.engine, self.nEnts, pos = pos, heading = heading)
        print "EntMgr created: ", ent.uiname, ent.eid, self.nEnts
        ent.initAspects()
        self.ents[self.nEnts] = ent;
        self.selectedEnt = ent
        self.selectedEntIndex = self.nEnts;

        self.nEnts = self.nEnts + 1
        return ent

    def selectNextEnt(self):
        if self.selectedEntIndex >= self.nEnts - 1:
            self.selectedEntIndex = 0
        else:
            self.selectedEntIndex += 1
        self.selectedEnt = self.ents[self.selectedEntIndex]
        print "EntMgr selected: ", str(self.selectedEnt)
        return self.selectedEnt

    def getSelected(self):
        return self.selectedEnt


    def tick(self, dt):
        for eid, ent in self.ents.iteritems():
            ent.tick(dt)
        

