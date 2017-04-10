package main

import "fmt"
import "github.com/xmonader/flabtut/graphics"
import "github.com/google/flatbuffers/go"

func pack() []byte {
	b:=&flatbuffers.Builder{}
	graphics.Vec2DStart(b)
	graphics.Vec2DAddP1(b, graphics.CreatePoint2D(b, 3, 5))
	graphics.Vec2DAddP2(b, graphics.CreatePoint2D(b, 9, 9))
	pos:=graphics.Vec2DEnd(b)
	b.Finish(pos)
	return b.Bytes[b.Head():]
}
func read(buf []byte) {
	vec2d:=graphics.GetRootAsVec2D(buf, 0)
	p1:=vec2d.P1(nil)
	p2:=vec2d.P2(nil)
	fmt.Println(p1.X(), p1.Y(), p2.X(), p2.Y())
}
func main() {
	read(pack())
}
