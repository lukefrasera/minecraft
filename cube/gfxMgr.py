# Graphics manager
import ogre.renderer.OGRE as ogre

from mgr import Mgr

# Manages graphics. Creates graphics, scene, scene nodes, renders scene
class GfxMgr(Mgr):
    def __init__(self, engine):
        Mgr.__init__(self, engine)
        pass

    def initialize(self):
        self.createRoot()
        self.defineResources()
        self.setupRenderSystem()
        self.createRenderWindow()
        self.initializeResourceGroups()
        self.setupScene()


    def loadLevel(self):
        pass

    def releaseLevel(self):
        self.cleanUp()

    def tick(self, dtime):
        self.root.renderOneFrame()


    # The Root constructor for the ogre
    def createRoot(self):
        self.root = ogre.Root()
 
    # Here the resources are read from the resources.cfg
    def defineResources(self):
        cf = ogre.ConfigFile()
        cf.load("resources.cfg")
 
        seci = cf.getSectionIterator()
        while seci.hasMoreElements():
            secName = seci.peekNextKey()
            settings = seci.getNext()
 
            for item in settings:
                typeName = item.key
                archName = item.value
                ogre.ResourceGroupManager.getSingleton().addResourceLocation(archName, typeName, secName)
 
    # Create and configure the rendering system (either DirectX or OpenGL) here
    def setupRenderSystem(self):
        if not self.root.restoreConfig() and not self.root.showConfigDialog():
            raise Exception("User canceled the config dialog -> Application.setupRenderSystem()")
 
 
    # Create the render window
    def createRenderWindow(self):
        self.renderWindow = self.root.initialise(True, "CS 381 Spring 2012 Engine Version 1.0")
 
    # Initialize the resources here (which were read from resources.cfg in defineResources()
    def initializeResourceGroups(self):
        ogre.TextureManager.getSingleton().setDefaultNumMipmaps(5)
        ogre.ResourceGroupManager.getSingleton().initialiseAllResourceGroups()
 
    # Now, create a scene here. Three things that MUST BE done are sceneManager, camera and
    # viewport initializations
    def setupScene(self):
        self.sceneManager = self.root.createSceneManager(ogre.ST_GENERIC, "Default SceneManager")

        self.camera = self.sceneManager.createCamera("Camera")
        self.camera.nearClipDistance = 2

        self.viewPort = self.root.getAutoCreatedWindow().addViewport(self.camera)
        self.sceneManager.ambientLight = 100,100,100
 
        # Setup a ground plane.
        #plane = ogre.Plane ((0, 1, 0), -100)
        #plane = ogre.Plane ((0, 1, 0), 0)
        self.groundPlane = ogre.Plane ((0, 1, 0), 0)
        meshManager = ogre.MeshManager.getSingleton ()
        meshManager.createPlane ('Ground', 'General', self.groundPlane,
                                     100, 100, 20, 20, True, 1, 5, 5, (0, 0, 1))
        ent = self.sceneManager.createEntity('GroundEntity', 'Ground')
        self.sceneManager.getRootSceneNode().createChildSceneNode ().attachObject (ent)
        ent.setMaterialName ('1335851461_1_outline.png' )
        #self.sceneManager.setSkyBox (True, "Examples/MorningSkyBox", 5000, False)
        self.camYawNode = self.sceneManager.getRootSceneNode().createChildSceneNode('CamNode1',
                                                                    #(-400, 200, 400))
                                                                    (0, 8, 0))
        #node.yaw(ogre.Degree(-45))
        self.camYawNode.yaw(ogre.Degree(0))
        self.camera.lookAt((0,0,0))
        self.camPitchNode = self.camYawNode.createChildSceneNode('PitchNode1')
        self.camPitchNode.attachObject(self.camera)
        self.camPitchNode.pitch(ogre.Degree(-90))
 
 
     # In the end, clean everything up (= delete)
    def cleanUp(self):
         pass
         #del self.root

