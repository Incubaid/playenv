# automatically generated, do not modify

# namespace: data

import flatbuffers

class Message(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMessage(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Message()
        x.Init(buf, n + offset)
        return x


    # Message
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Message
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Message
    def Subject(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # Message
    def Body(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

def MessageStart(builder): builder.StartObject(3)
def MessageAddId(builder, id): builder.PrependInt32Slot(0, id, 0)
def MessageAddSubject(builder, subject): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(subject), 0)
def MessageAddBody(builder, body): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(body), 0)
def MessageEnd(builder): return builder.EndObject()
