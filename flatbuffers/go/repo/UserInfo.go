// automatically generated, do not modify

package repo

import (
	flatbuffers "github.com/google/flatbuffers/go"
)
type UserInfo struct {
	_tab flatbuffers.Table
}

func (rcv *UserInfo) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *UserInfo) Id() int32 {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		return rcv._tab.GetInt32(o + rcv._tab.Pos)
	}
	return 0
}

func (rcv *UserInfo) Name() []byte {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(6))
	if o != 0 {
		return rcv._tab.ByteVector(o + rcv._tab.Pos)
	}
	return nil
}

func UserInfoStart(builder *flatbuffers.Builder) { builder.StartObject(2) }
func UserInfoAddId(builder *flatbuffers.Builder, id int32) { builder.PrependInt32Slot(0, id, 0) }
func UserInfoAddName(builder *flatbuffers.Builder, name flatbuffers.UOffsetT) { builder.PrependUOffsetTSlot(1, flatbuffers.UOffsetT(name), 0) }
func UserInfoEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT { return builder.EndObject() }
