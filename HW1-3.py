import math

def check_equal(x, y, msg=None):
    if x == y:
        if msg is None:
            print("Success")
        else:
            print(msg, ": Success")
    else:
        if msg is None:
            print("Error:")
        else:
            print("Error in", msg, ":")
        print("    Your answer was:", x)
        print("    Correct answer: ", y)
    assert x == y, "%r and %r are different" % (x, y)

class Square(object):
    
    def __init__(self, center, edge):
        assert isinstance(center, tuple)
        assert len(center) == 2
        self.center = center
        self.semiedge = edge / 2
        
    @property
    def edge(self):
        return 2 * semiedge
    
    @property
    def ur(self):
        """Returns the coordinates of the upper right corner."""
        (x, y) = self.center
        return x + self.semiedge, y + self.semiedge
    
    @property
    def lr(self):
        """Returns the coordinates of the upper right corner."""
        (x, y) = self.center
        return x + self.semiedge, y - self.semiedge

    @property
    def ul(self):
        """Returns the coordinates of the upper right corner."""
        (x, y) = self.center
        return x - self.semiedge, y + self.semiedge

    @property
    def ll(self):
        """Returns the coordinates of the upper right corner."""
        (x, y) = self.center
        return x - self.semiedge, y - self.semiedge
    
    def contains(self, point):
        """Returns whether the point is in the square."""
        x, y = point
        cx, cy = self.center
        return abs(x - cx) < self.semiedge and abs(y - cy) < self.semiedge

class Circle(object):

    def __init__(self,center,radius):
        assert isinstance(center,tuple)
        assert len(center)==2
        self.center=center
        self.radius=radius

    def radius(self):
        return radius

    def ax(self):
        (x,y)=self.center
        return x+self.radius

    def bx(self):
        (x,y)=self.center
        return x-self.radius

    def ay(self):
        (x,y)=self.center
        return y+self.radius

    def by(self):
        (x,y)=self.center
        return x-self.radius

    def contains(self,x):
        if isinstance(x,Square):
            return self.contains_square(x)
        elif isinstance(x,Circle):
            return abs(math.sqrt((x.ax()-self.ax())**2+(x.ay()-self.ay())**2)+x.radius)<=self.radius
        else:
            return self.contains_point(x)

    def contains_point(self,p):
        x,y=p
        cx,cy=self.center
        return abs(math.sqrt((x-cx)**2+(y-cy)**2))<=self.radius

    def contains_square(self,s):
        urx,ury=s.ur
        cx,cy=self.center
        return abs(math.sqrt((cx-urx)**2+(cy-ury)**2))<=self.radius

c = Circle((1, 2), 4)
check_equal(c.contains_point((2, 2)), True)
check_equal(c.contains_point((10, 20)), False)

c = Circle((1, 2), 4)
s1 = Square((2, 2), 1)
s2 = Square((3, 2), 6)
check_equal(c.contains_square(s1), True)
check_equal(c.contains_square(s2), False)

c1 = Circle((1, 2), 4)
c2 = Circle((1, 2), 4)
c3 = Circle((2, 2), 3)
c4 = Circle((2, 2), 4)
s1 = Square((2, 2), 1)
s2 = Square((3, 2), 6)
p1 = (2, 3)
p2 = (3, 4)
p3 = (4, 5)

check_equal(c1.contains(p1), True, msg="a")
check_equal(c1.contains(p2), True, msg="b")
check_equal(c1.contains(p3), False, msg="c")
check_equal(c1.contains(s1), True, msg="d")
check_equal(c1.contains(s2), False, msg="e")
check_equal(c1.contains(c2), True, msg="f")
check_equal(c1.contains(c3), True, msg="g")
check_equal(c1.contains(c4), False, msg="h")

