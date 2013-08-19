# Input manager. Initialize and manage keyboard and mouse. Buffered and unbuffered input
import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS


from mgr import Mgr
from vector import Vector3

from unitAI import UnitAI
from command import Target, Move, Ram

class InputMgr(Mgr, OIS.KeyListener, OIS.MouseListener, OIS.JoyStickListener):
    def __init__(self, engine):
        Mgr.__init__(self, engine)
        OIS.KeyListener.__init__(self)
        OIS.MouseListener.__init__(self)
        OIS.JoyStickListener.__init__(self)
        self.move = 5
        self.rotate = 0.01
        self.yawRot = 0.0
        self.pitchRot = 0.0
        self.transVector = ogre.Vector3(0, 0, 0)
        self.toggle = 0.1
        self.distanceSquaredThreshold = 10000
        self.leftShiftDown = False;
        self.cameraToggle = False;
        pass


    def initialize(self):
        windowHandle = 0
        renderWindow = self.engine.gfxMgr.root.getAutoCreatedWindow()
        windowHandle = renderWindow.getCustomAttributeInt("WINDOW")
        paramList = [("WINDOW", str(windowHandle))]
        paramList.append(("x11_keyboard_grab", "false"))
        self.inputManager = OIS.createPythonInputSystem(paramList)
 
        # Now InputManager is initialized for use. Keyboard and Mouse objects
        # must still be initialized separately
        self.keyboard = None
        try:
            self.keyboard = self.inputManager.createInputObjectKeyboard(OIS.OISKeyboard, True)
        except Exception, e:
            print "No Keyboard or mouse!!!!"
            raise e
        if self.keyboard:
            self.keyboard.setEventCallback(self)
 
        self.transVector = ogre.Vector3(0, 0, 0)

        import random
        self.randomizer = random
        self.randomizer.seed(None)

        print "Initialized Input Manager"
        

    def crosslink(self):
        self.camera = self.engine.gfxMgr.camera
        self.camYawNode = self.engine.gfxMgr.camYawNode
        self.camPitchNode = self.engine.gfxMgr.camPitchNode


    def releaseLevel(self):
        self.inputManager.destroyInputObjectKeyboard(self.keyboard)
        OIS.InputManager.destroyInputSystem(self.inputManager)
        self.inputManager = None
        
    def tick(self, dtime):
        self.keyboard.capture()

        self.keyPressed(dtime)
        
        #self.camNode.yaw(ogre.Degree(-self.yawRot)
        self.camYawNode.yaw(ogre.Radian(self.yawRot))
        self.camPitchNode.pitch(ogre.Radian(self.pitchRot))

        # Translate the camera based on time.
        self.camYawNode.translate(self.camYawNode.orientation
                               * self.transVector
                               * dtime)

        self.handleCreateEnt(dtime)
        pass

    def handleCreateEnt(self, dt):
        self.toggle = self.toggle - dt
        if self.keyboard.isKeyDown(OIS.KC_EQUALS) and self.toggle < 0.0:
            ent = self.engine.entMgr.createEnt(self.randomizer.choice(self.engine.entMgr.entTypes), pos = Vector3(0,0,0))
            self.toggle = 0.1

    def keyPressed(self, evt):
        # Move the camera using keyboard input.
        self.transVector = ogre.Vector3(0, 0, 0)
        self.yawRot = 0.0
        self.pitchRot = 0.0
        # Forward.
        if self.keyboard.isKeyDown(OIS.KC_W):
            self.transVector.z -= self.move
        # Backward.
        if self.keyboard.isKeyDown(OIS.KC_S):
            self.transVector.z += self.move
        # Left.
        if self.keyboard.isKeyDown(OIS.KC_A):
            self.transVector.x -= self.move
        # Right.
        if  self.keyboard.isKeyDown(OIS.KC_D):
            self.transVector.x += self.move
        # Up.        
        if self.keyboard.isKeyDown(OIS.KC_PGUP):
            self.transVector.y += self.move
        # Down.
        if self.keyboard.isKeyDown(OIS.KC_PGDOWN):
            self.transVector.y -= self.move          

        if self.keyboard.isKeyDown(OIS.KC_Q):
            self.yawRot = self.rotate

        if self.keyboard.isKeyDown(OIS.KC_E):
            self.yawRot = -self.rotate

        if self.keyboard.isKeyDown(OIS.KC_Z):
            self.pitchRot = self.rotate

        if self.keyboard.isKeyDown(OIS.KC_X):
            self.pitchRot = -self.rotate

        if self.keyboard.isKeyDown(OIS.KC_LSHIFT):
            self.leftShiftDown = True
        else:
            self.leftShiftDown = False

        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_TAB):
            self.toggle = 0.5
            if self.cameraToggle:
                self.camYawNode.resetOrientation()
                self.cameraToggle = False
                self.camYawNode.position = Vector3(0,10,0 )
                self.camYawNode.pitch(ogre.Degree(0))

            else:
                self.camYawNode.resetOrientation()
                self.cameraToggle = True
                self.camYawNode.position = self.engine.entMgr.selectedEnt.pos + Vector3(0,1,0)
                self.camYawNode.pitch(ogre.Degree(90))

            # Faster
        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_UP):
            self.toggle = 0.8
            invalid = False
            for vector in self.engine.gameMgr.invalid:
            	if self.engine.entMgr.selectedEnt.pos + Vector3(0,0,-1) == vector:
                    invalid = True
            if not invalid:
                self.engine.entMgr.selectedEnt.desiredpos += Vector3(0,0,-1)

            # Slower
        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_DOWN):
            self.toggle = 0.8
            invalid = False
            for vector in self.engine.gameMgr.invalid:
            	if self.engine.entMgr.selectedEnt.pos + Vector3(0,0,1) == vector:
                    invalid = True
            if not invalid:
                self.engine.entMgr.selectedEnt.desiredpos += Vector3(0,0,1)

            # turn left
        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_LEFT):
            self.toggle = 0.8
            invalid = False
            for vector in self.engine.gameMgr.invalid:
            	if self.engine.entMgr.selectedEnt.pos + Vector3(-1,0,0) == vector:
                    invalid = True
            if not invalid:
                self.engine.entMgr.selectedEnt.desiredpos += Vector3(-1,0,0)


            # turn right
        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_RIGHT):
            self.toggle = 0.8
            invalid = False
            for vector in self.engine.gameMgr.invalid:
            	if self.engine.entMgr.selectedEnt.pos + Vector3(1,0,0) == vector:
                    invalid = True
            if not invalid:
                self.engine.entMgr.selectedEnt.desiredpos += Vector3(1,0,0)

        if self.keyboard.isKeyDown(OIS.KC_ESCAPE):
            self.engine.stop()

        return True

    def keyReleased(self, evt):
        return True
    
       # JoystickListener
    def buttonPressed(self, evt, button):
        return True
    def buttonReleased(self, evt, button):
        return True
    def axisMoved(self, evt, axis):
        return True

#---------------------------------------------------------------------------------------------------
