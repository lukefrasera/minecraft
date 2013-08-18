# Render code for renderables
# vel is rate of change of pos
# Sushil Louis
from aspect import Aspect
#from collections import deque

class UnitAI(Aspect):
    def __init__(self, ent):
        Aspect.__init__(self, ent)
        self.commands = []

    def initialize(self):
        self.commands = []


    def tick(self, dtime):
        #---------------------------------------------
        if self.commands:
            currentCommand = self.commands[0]
            currentCommand.tick(dtime)
            if currentCommand.done():
                cmd = self.commands.pop(0)
                print "done with: ", cmd.name, cmd.target
                if (self.commands):
                    self.commands[0].init()
                    print "Initializing", self.commands[0].name
        #---------------------------------------------

    def addCommand(self, command):
        self.commands.append(command)

    def setCommand(self, command):
        self.commands = [command,]
        command.init()

