# automatically generated, do not modify

# namespace: graphics

import flatbuffers

class Point2D(object):
    __slots__ = ['_tab']

    # Point2D
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Point2D
    def X(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # Point2D
    def Y(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))

def CreatePoint2D(builder, x, y):
    builder.Prep(4, 8)
    builder.PrependInt32(y)
    builder.PrependInt32(x)
    return builder.Offset()
