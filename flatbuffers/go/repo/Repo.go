// automatically generated, do not modify

package repo

import (
	flatbuffers "github.com/google/flatbuffers/go"
)
type Repo struct {
	_tab flatbuffers.Table
}

func GetRootAsRepo(buf []byte, offset flatbuffers.UOffsetT) *Repo {
	n := flatbuffers.GetUOffsetT(buf[offset:])
	x := &Repo{}
	x.Init(buf, n + offset)
	return x
}

func (rcv *Repo) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *Repo) Id() int32 {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		return rcv._tab.GetInt32(o + rcv._tab.Pos)
	}
	return 0
}

func (rcv *Repo) Name() []byte {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(6))
	if o != 0 {
		return rcv._tab.ByteVector(o + rcv._tab.Pos)
	}
	return nil
}

func (rcv *Repo) Language() int8 {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(8))
	if o != 0 {
		return rcv._tab.GetInt8(o + rcv._tab.Pos)
	}
	return 0
}

func (rcv *Repo) Files(j int) []byte {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(10))
	if o != 0 {
		a := rcv._tab.Vector(o)
		return rcv._tab.ByteVector(a + flatbuffers.UOffsetT(j * 4))
	}
	return nil
}

func (rcv *Repo) FilesLength() int {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(10))
	if o != 0 {
		return rcv._tab.VectorLen(o)
	}
	return 0
}

func RepoStart(builder *flatbuffers.Builder) { builder.StartObject(4) }
func RepoAddId(builder *flatbuffers.Builder, id int32) { builder.PrependInt32Slot(0, id, 0) }
func RepoAddName(builder *flatbuffers.Builder, name flatbuffers.UOffsetT) { builder.PrependUOffsetTSlot(1, flatbuffers.UOffsetT(name), 0) }
func RepoAddLanguage(builder *flatbuffers.Builder, language int8) { builder.PrependInt8Slot(2, language, 0) }
func RepoAddFiles(builder *flatbuffers.Builder, files flatbuffers.UOffsetT) { builder.PrependUOffsetTSlot(3, flatbuffers.UOffsetT(files), 0) }
func RepoStartFilesVector(builder *flatbuffers.Builder, numElems int) flatbuffers.UOffsetT { return builder.StartVector(4, numElems, 4)
}
func RepoEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT { return builder.EndObject() }
