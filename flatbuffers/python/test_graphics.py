from graphics.Point2D import *
from graphics.Vec2D import *
from flatbuffers import Builder

def packmsg():
    b=Builder(0)
	#Create the field and add it directly.
    Vec2DStart(b)
    p1= CreatePoint2D(b, 3, 5)
    Vec2DAddP1(b, p1)
    p2= CreatePoint2D(b, 9, 15)
    Vec2DAddP2(b, p2)
    
    #Vec2DAddP1(b, CreatePoint2D(b, 3, 5))
    #Vec2DAddP2(b, CreatePoint2D(b, 9, 15))
    pos=Vec2DEnd(b)
    b.Finish(pos)
    return b.Output()

def readmsg(buf):
    v=Vec2D.GetRootAsVec2D(buf, 0)
    print(v.P1(), v.P2())



if __name__=="__main__":
    readmsg(packmsg())
