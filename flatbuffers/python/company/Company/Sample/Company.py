# automatically generated, do not modify

# namespace: Sample

import flatbuffers

class Company(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCompany(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Company()
        x.Init(buf, n + offset)
        return x


    # Company
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Company
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # Company
    def Branches(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Branch import Branch
            obj = Branch()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Company
    def BranchesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def CompanyStart(builder): builder.StartObject(2)
def CompanyAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def CompanyAddBranches(builder, branches): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(branches), 0)
def CompanyStartBranchesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CompanyEnd(builder): return builder.EndObject()
