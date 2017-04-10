# automatically generated, do not modify

# namespace: repo

import flatbuffers

class UserInfo(object):
    __slots__ = ['_tab']

    # UserInfo
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserInfo
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserInfo
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

def UserInfoStart(builder): builder.StartObject(2)
def UserInfoAddId(builder, id): builder.PrependInt32Slot(0, id, 0)
def UserInfoAddName(builder, name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def UserInfoEnd(builder): return builder.EndObject()
