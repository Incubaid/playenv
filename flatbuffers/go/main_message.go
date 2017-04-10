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
