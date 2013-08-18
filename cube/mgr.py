
class Mgr(object):
    def __init__(self, engine):
        self.engine = engine
        pass

    def initialize(self):
        print "Initializing: ", type(self).__name__
        pass

    def crosslink(self):
        pass

    def loadLevel(self):
        pass

    def releaseLevel(self):
        pass

    def tick(self, dtime):
        pass

    def render(self):
        pass

