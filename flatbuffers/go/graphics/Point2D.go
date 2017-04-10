// automatically generated, do not modify

package graphics

import (
	flatbuffers "github.com/google/flatbuffers/go"
)
type Point2D struct {
	_tab flatbuffers.Struct
}

func (rcv *Point2D) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *Point2D) X() int32 { return rcv._tab.GetInt32(rcv._tab.Pos + flatbuffers.UOffsetT(0)) }
func (rcv *Point2D) Y() int32 { return rcv._tab.GetInt32(rcv._tab.Pos + flatbuffers.UOffsetT(4)) }

func CreatePoint2D(builder *flatbuffers.Builder, x int32, y int32) flatbuffers.UOffsetT {
    builder.Prep(4, 8)
    builder.PrependInt32(y)
    builder.PrependInt32(x)
    return builder.Offset()
}
