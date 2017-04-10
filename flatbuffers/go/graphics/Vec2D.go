// automatically generated, do not modify

package graphics

import (
	flatbuffers "github.com/google/flatbuffers/go"
)
type Vec2D struct {
	_tab flatbuffers.Table
}

func GetRootAsVec2D(buf []byte, offset flatbuffers.UOffsetT) *Vec2D {
	n := flatbuffers.GetUOffsetT(buf[offset:])
	x := &Vec2D{}
	x.Init(buf, n + offset)
	return x
}

func (rcv *Vec2D) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *Vec2D) P1(obj *Point2D) *Point2D {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		x := o + rcv._tab.Pos
		if obj == nil {
			obj = new(Point2D)
		}
		obj.Init(rcv._tab.Bytes, x)
		return obj
	}
	return nil
}

func (rcv *Vec2D) P2(obj *Point2D) *Point2D {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(6))
	if o != 0 {
		x := o + rcv._tab.Pos
		if obj == nil {
			obj = new(Point2D)
		}
		obj.Init(rcv._tab.Bytes, x)
		return obj
	}
	return nil
}

func Vec2DStart(builder *flatbuffers.Builder) { builder.StartObject(2) }
func Vec2DAddP1(builder *flatbuffers.Builder, p1 flatbuffers.UOffsetT) { builder.PrependStructSlot(0, flatbuffers.UOffsetT(p1), 0) }
func Vec2DAddP2(builder *flatbuffers.Builder, p2 flatbuffers.UOffsetT) { builder.PrependStructSlot(1, flatbuffers.UOffsetT(p2), 0) }
func Vec2DEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT { return builder.EndObject() }
