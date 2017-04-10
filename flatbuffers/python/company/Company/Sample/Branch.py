# automatically generated, do not modify

# namespace: Sample

import flatbuffers

class Branch(object):
    __slots__ = ['_tab']

    # Branch
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Branch
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # Branch
    def Address(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # Branch
    def Field(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def BranchStart(builder): builder.StartObject(3)
def BranchAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def BranchAddAddress(builder, address): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(address), 0)
def BranchAddField(builder, field): builder.PrependInt8Slot(2, field, 0)
def BranchEnd(builder): return builder.EndObject()
