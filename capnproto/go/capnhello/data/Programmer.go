package data

// AUTO GENERATED - DO NOT EDIT

import (
	capnp "zombiezen.com/go/capnproto2"
)

type Programmer struct{ capnp.Struct }

func NewProgrammer(s *capnp.Segment) (Programmer, error) {
	st, err := capnp.NewStruct(s, capnp.ObjectSize{DataSize: 0, PointerCount: 3})
	if err != nil {
		return Programmer{}, err
	}
	return Programmer{st}, nil
}

func NewRootProgrammer(s *capnp.Segment) (Programmer, error) {
	st, err := capnp.NewRootStruct(s, capnp.ObjectSize{DataSize: 0, PointerCount: 3})
	if err != nil {
		return Programmer{}, err
	}
	return Programmer{st}, nil
}

func ReadRootProgrammer(msg *capnp.Message) (Programmer, error) {
	root, err := msg.RootPtr()
	if err != nil {
		return Programmer{}, err
	}
	return Programmer{root.Struct()}, nil
}
func (s Programmer) Name() (string, error) {
	p, err := s.Struct.Ptr(0)
	if err != nil {
		return "", err
	}
	return p.Text(), nil
}

func (s Programmer) HasName() bool {
	p, err := s.Struct.Ptr(0)
	return p.IsValid() || err != nil
}

func (s Programmer) NameBytes() ([]byte, error) {
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

func (s Programmer) SetName(v string) error {
	t, err := capnp.NewText(s.Struct.Segment(), v)
	if err != nil {
		return err
	}
	return s.Struct.SetPtr(0, t.List.ToPtr())
}

func (s Programmer) Email() (string, error) {
	p, err := s.Struct.Ptr(1)
	if err != nil {
		return "", err
	}
	return p.Text(), nil
}

func (s Programmer) HasEmail() bool {
	p, err := s.Struct.Ptr(1)
	return p.IsValid() || err != nil
}

func (s Programmer) EmailBytes() ([]byte, error) {
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

func (s Programmer) SetEmail(v string) error {
	t, err := capnp.NewText(s.Struct.Segment(), v)
	if err != nil {
		return err
	}
	return s.Struct.SetPtr(1, t.List.ToPtr())
}

func (s Programmer) Likes() (capnp.TextList, error) {
	p, err := s.Struct.Ptr(2)
	if err != nil {
		return capnp.TextList{}, err
	}
	return capnp.TextList{List: p.List()}, nil
}

func (s Programmer) HasLikes() bool {
	p, err := s.Struct.Ptr(2)
	return p.IsValid() || err != nil
}

func (s Programmer) SetLikes(v capnp.TextList) error {
	return s.Struct.SetPtr(2, v.List.ToPtr())
}

// NewLikes sets the likes field to a newly
// allocated capnp.TextList, preferring placement in s's segment.
func (s Programmer) NewLikes(n int32) (capnp.TextList, error) {
	l, err := capnp.NewTextList(s.Struct.Segment(), n)
	if err != nil {
		return capnp.TextList{}, err
	}
	err = s.Struct.SetPtr(2, l.List.ToPtr())
	return l, err
}

// Programmer_List is a list of Programmer.
type Programmer_List struct{ capnp.List }

// NewProgrammer creates a new list of Programmer.
func NewProgrammer_List(s *capnp.Segment, sz int32) (Programmer_List, error) {
	l, err := capnp.NewCompositeList(s, capnp.ObjectSize{DataSize: 0, PointerCount: 3}, sz)
	if err != nil {
		return Programmer_List{}, err
	}
	return Programmer_List{l}, nil
}

func (s Programmer_List) At(i int) Programmer           { return Programmer{s.List.Struct(i)} }
func (s Programmer_List) Set(i int, v Programmer) error { return s.List.SetStruct(i, v.Struct) }

// Programmer_Promise is a wrapper for a Programmer promised by a client call.
type Programmer_Promise struct{ *capnp.Pipeline }

func (p Programmer_Promise) Struct() (Programmer, error) {
	s, err := p.Pipeline.Struct()
	return Programmer{s}, err
}
