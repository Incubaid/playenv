# automatically generated, do not modify

# namespace: repo

import flatbuffers

class Repo(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRepo(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Repo()
        x.Init(buf, n + offset)
        return x


    # Repo
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Repo
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Repo
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # Repo
    def Language(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # Repo
    def Files(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Repo
    def FilesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def RepoStart(builder): builder.StartObject(4)
def RepoAddId(builder, id): builder.PrependInt32Slot(0, id, 0)
def RepoAddName(builder, name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def RepoAddLanguage(builder, language): builder.PrependInt8Slot(2, language, 0)
def RepoAddFiles(builder, files): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(files), 0)
def RepoStartFilesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def RepoEnd(builder): return builder.EndObject()
