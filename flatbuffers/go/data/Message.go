// automatically generated, do not modify

package data

import (
	flatbuffers "github.com/google/flatbuffers/go"
)
type Message struct {
	_tab flatbuffers.Table
}

func GetRootAsMessage(buf []byte, offset flatbuffers.UOffsetT) *Message {
	n := flatbuffers.GetUOffsetT(buf[offset:])
	x := &Message{}
	x.Init(buf, n + offset)
	return x
}

func (rcv *Message) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *Message) Id() int32 {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		return rcv._tab.GetInt32(o + rcv._tab.Pos)
	}
	return 0
}

func (rcv *Message) Subject() []byte {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(6))
	if o != 0 {
		return rcv._tab.ByteVector(o + rcv._tab.Pos)
	}
	return nil
}

func (rcv *Message) Body() []byte {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(8))
	if o != 0 {
		return rcv._tab.ByteVector(o + rcv._tab.Pos)
	}
	return nil
}

func MessageStart(builder *flatbuffers.Builder) { builder.StartObject(3) }
func MessageAddId(builder *flatbuffers.Builder, id int32) { builder.PrependInt32Slot(0, id, 0) }
func MessageAddSubject(builder *flatbuffers.Builder, subject flatbuffers.UOffsetT) { builder.PrependUOffsetTSlot(1, flatbuffers.UOffsetT(subject), 0) }
func MessageAddBody(builder *flatbuffers.Builder, body flatbuffers.UOffsetT) { builder.PrependUOffsetTSlot(2, flatbuffers.UOffsetT(body), 0) }
func MessageEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT { return builder.EndObject() }
