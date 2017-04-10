# automatically generated, do not modify

# namespace: graphics

import flatbuffers

class Vec2D(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsVec2D(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Vec2D()
        x.Init(buf, n + offset)
        return x


    # Vec2D
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Vec2D
    def P1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from .Point2D import Point2D
            obj = Point2D()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Vec2D
    def P2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = o + self._tab.Pos
            from .Point2D import Point2D
            obj = Point2D()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def Vec2DStart(builder): builder.StartObject(2)
def Vec2DAddP1(builder, p1): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(p1), 0)
def Vec2DAddP2(builder, p2): builder.PrependStructSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(p2), 0)
def Vec2DEnd(builder): return builder.EndObject()
