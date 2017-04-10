# Go-FlatBuffers
FlatBuffers is an efficient cross platform serialization library for C++, C#, C, Go, Java, JavaScript, PHP, and Python. It was originally created at Google for game development and other performance-critical applications.

Pros:
- Does the Job
- Fast (Due to its random access feature as It doesn't `parse` the data first).

Cons:
- Counter intuitive.
- Speed above all (even readability) and unclear errors with some straightforward usage. 
    
## Installation
- Very Straightforward as specified in its website
- Get the go package 
    ```
    go get github.com/google/flatbuffers/go
    ```

## How to use it
### Examples
#### Message 
1- You need to define the schema first. That's the easy part.
```
namespace data;

table Message{
	id:int;
	subject:string;
	body:string;
}

root_type Message;
```
Note:
- table maps to an object (something gonna change).
- namespace maps to a package.
- root_type: Gives you the entry point of the data (and it can't be a struct).

To generate data package with Message.go. 
```
$ flatc message.fbs --go
```
Message.go
```go
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

```

main.go

```go
package main

import "fmt"
import "github.com/xmonader/flabtut/data"
import "github.com/google/flatbuffers/go"

func pack() []byte {
	b:=&flatbuffers.Builder{}
    subj:=b.CreateString("Hello")
    body:=b.CreateString("This is the body")
    
    data.MessageStart(b)
    data.MessageAddId(b, 32)
    data.MessageAddSubject(b, subj)
    data.MessageAddBody(b, body)
	pos:=data.MessageEnd(b)
	b.Finish(pos)
	return b.Bytes[b.Head():]
}
func read(buf []byte) {
	m:=data.GetRootAsMessage(buf, 0)
    fmt.Println("Message: ", m.Id(), string(m.Subject()), string(m.Body()))
}
func main() {
	read(pack())
}


```
1- Imports
```go
import "github.com/xmonader/flabtut/data"
import "github.com/google/flatbuffers/go"
```
- flabtut/data is our generated package that maps the schema to a kinda-object 
- flatbuffers/go is the interface to flatbuffers library 

2- Packing the data
- FlatBuffers uses the builder pattern to create the `Message` to be serialized
```go
	b:=&flatbuffers.Builder{}
```
- Create the fields first
```go
    subj:=b.CreateString("Hello")
    body:=b.CreateString("This is the body")
```
- Build your data (Between MessageStart, MessageEnd) and always maintain the position that Message ends at (to finish the builder)
```go

    data.MessageStart(b)
    data.MessageAddId(b, 32)
    data.MessageAddSubject(b, subj)
    data.MessageAddBody(b, body)
	pos:=data.MessageEnd(b)

```
- Finish the builder 
```go
	b.Finish(pos)
	return b.Bytes[b.Head()]:]
```
The `Head` call is to reference the start of the `useful data`  

3- Reading the data
- Load the data and GetItsRootAs* 
```go
func read(buf []byte) {
	m:=data.GetRootAsMessage(buf, 0)
}
```
- Access the Message data (Randomly) without needing to `parse` it (thanks to the offsets)
```go
    fmt.Println("Message: ", m.Id(), string(m.Subject()), string(m.Body()))
```

4- Main
```go

func main() {
	read(pack())
}

```


#### Graphics example
1- Schema
```
namespace graphics;

struct Point2D{
    x:int;
    y:int;
}
table Vec2D{
    p1: Point2D;
    p2: Point2D;
}


root_type Vec2D;

```
2- Create package graphics with (Point2D.go, Vec2D.go)
```
flatc graphics.fbs --go
```
- Point2D
```go
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


```
- Vec2D.go
```go
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

```
- Main file
```go
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

```
