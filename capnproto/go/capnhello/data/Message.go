package data

// AUTO GENERATED - DO NOT EDIT

import (
	capnp "zombiezen.com/go/capnproto2"
)

type Message struct{ capnp.Struct }

func NewMessage(s *capnp.Segment) (Message, error) {
	st, err := capnp.NewStruct(s, capnp.ObjectSize{DataSize: 8, PointerCount: 2})
	if err != nil {
		return Message{}, err
	}
	return Message{st}, nil
}

func NewRootMessage(s *capnp.Segment) (Message, error) {
	st, err := capnp.NewRootStruct(s, capnp.ObjectSize{DataSize: 8, PointerCount: 2})
	if err != nil {
		return Message{}, err
	}
	return Message{st}, nil
}

func ReadRootMessage(msg *capnp.Message) (Message, error) {
	root, err := msg.RootPtr()
	if err != nil {
		return Message{}, err
	}
	return Message{root.Struct()}, nil
}
func (s Message) Id() int64 {
	return int64(s.Struct.Uint64(0))
}

func (s Message) SetId(v int64) {
	s.Struct.SetUint64(0, uint64(v))
}

func (s Message) Subject() (string, error) {
	p, err := s.Struct.Ptr(0)
	if err != nil {
		return "", err
	}
	return p.Text(), nil
}

func (s Message) HasSubject() bool {
	p, err := s.Struct.Ptr(0)
	return p.IsValid() || err != nil
}

func (s Message) SubjectBytes() ([]byte, error) {
	p, err := s.Struct.Ptr(0)
	if err != nil {
		return nil, err
	}
	d := p.Data()
	if len(d) == 0 {
		return d, nil
	}
	return d[:len(d)-1], nil
}

func (s Message) SetSubject(v string) error {
	t, err := capnp.NewText(s.Struct.Segment(), v)
	if err != nil {
		return err
	}
	return s.Struct.SetPtr(0, t.List.ToPtr())
}

func (s Message) Body() (string, error) {
	p, err := s.Struct.Ptr(1)
	if err != nil {
		return "", err
	}
	return p.Text(), nil
}

func (s Message) HasBody() bool {
	p, err := s.Struct.Ptr(1)
	return p.IsValid() || err != nil
}

func (s Message) BodyBytes() ([]byte, error) {
	p, err := s.Struct.Ptr(1)
	if err != nil {
		return nil, err
	}
	d := p.Data()
	if len(d) == 0 {
		return d, nil
	}
	return d[:len(d)-1], nil
}

func (s Message) SetBody(v string) error {
	t, err := capnp.NewText(s.Struct.Segment(), v)
	if err != nil {
		return err
	}
	return s.Struct.SetPtr(1, t.List.ToPtr())
}

// Message_List is a list of Message.
type Message_List struct{ capnp.List }

// NewMessage creates a new list of Message.
func NewMessage_List(s *capnp.Segment, sz int32) (Message_List, error) {
	l, err := capnp.NewCompositeList(s, capnp.ObjectSize{DataSize: 8, PointerCount: 2}, sz)
	if err != nil {
		return Message_List{}, err
	}
	return Message_List{l}, nil
}

func (s Message_List) At(i int) Message           { return Message{s.List.Struct(i)} }
func (s Message_List) Set(i int, v Message) error { return s.List.SetStruct(i, v.Struct) }

// Message_Promise is a wrapper for a Message promised by a client call.
type Message_Promise struct{ *capnp.Pipeline }

func (p Message_Promise) Struct() (Message, error) {
	s, err := p.Pipeline.Struct()
	return Message{s}, err
}
