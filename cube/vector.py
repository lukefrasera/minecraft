
import ogre.renderer.OGRE as ogre
Vector3  = ogre.Vector3


class point2(object):
    def __init__(self, x, y):
        assert type(x) is int and type(y) is int
        self.x = x
        self.y = y
    def __add__(self, rhs):
        assert type(rhs) is point2
        return point2(self.x + rhs.x, self.y + rhs.y)
    def __str__(self):
        return '%i,%i' % (self.x, self.y)
    __repr__ = __str__

