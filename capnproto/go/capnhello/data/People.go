package data

// AUTO GENERATED - DO NOT EDIT

import (
	capnp "zombiezen.com/go/capnproto2"
)

type Date struct{ capnp.Struct }

func NewDate(s *capnp.Segment) (Date, error) {
	st, err := capnp.NewStruct(s, capnp.ObjectSize{DataSize: 16, PointerCount: 0})
	if err != nil {
		return Date{}, err
	}
	return Date{st}, nil
}

func NewRootDate(s *capnp.Segment) (Date, error) {
	st, err := capnp.NewRootStruct(s, capnp.ObjectSize{DataSize: 16, PointerCount: 0})
	if err != nil {
		return Date{}, err
	}
	return Date{st}, nil
}

func ReadRootDate(msg *capnp.Message) (Date, error) {
	root, err := msg.RootPtr()
	if err != nil {
		return Date{}, err
	}
	return Date{root.Struct()}, nil
}
func (s Date) Year() int32 {
	return int32(s.Struct.Uint32(0))
}

func (s Date) SetYear(v int32) {
	s.Struct.SetUint32(0, uint32(v))
}

func (s Date) Month() int32 {
	return int32(s.Struct.Uint32(4))
}

func (s Date) SetMonth(v int32) {
	s.Struct.SetUint32(4, uint32(v))
}

func (s Date) Day() int32 {
	return int32(s.Struct.Uint32(8))
}

func (s Date) SetDay(v int32) {
	s.Struct.SetUint32(8, uint32(v))
}

// Date_List is a list of Date.
type Date_List struct{ capnp.List }

// NewDate creates a new list of Date.
func NewDate_List(s *capnp.Segment, sz int32) (Date_List, error) {
	l, err := capnp.NewCompositeList(s, capnp.ObjectSize{DataSize: 16, PointerCount: 0}, sz)
	if err != nil {
		return Date_List{}, err
	}
	return Date_List{l}, nil
}

func (s Date_List) At(i int) Date           { return Date{s.List.Struct(i)} }
func (s Date_List) Set(i int, v Date) error { return s.List.SetStruct(i, v.Struct) }

// Date_Promise is a wrapper for a Date promised by a client call.
type Date_Promise struct{ *capnp.Pipeline }

func (p Date_Promise) Struct() (Date, error) {
	s, err := p.Pipeline.Struct()
	return Date{s}, err
}

type Person struct{ capnp.Struct }

func NewPerson(s *capnp.Segment) (Person, error) {
	st, err := capnp.NewStruct(s, capnp.ObjectSize{DataSize: 0, PointerCount: 5})
	if err != nil {
		return Person{}, err
	}
	return Person{st}, nil
}

func NewRootPerson(s *capnp.Segment) (Person, error) {
	st, err := capnp.NewRootStruct(s, capnp.ObjectSize{DataSize: 0, PointerCount: 5})
	if err != nil {
		return Person{}, err
	}
	return Person{st}, nil
}

func ReadRootPerson(msg *capnp.Message) (Person, error) {
	root, err := msg.RootPtr()
	if err != nil {
		return Person{}, err
	}
	return Person{root.Struct()}, nil
}
func (s Person) Firstname() (string, error) {
	p, err := s.Struct.Ptr(0)
	if err != nil {
		return "", err
	}
	return p.Text(), nil
}

func (s Person) HasFirstname() bool {
	p, err := s.Struct.Ptr(0)
	return p.IsValid() || err != nil
}

func (s Person) FirstnameBytes() ([]byte, error) {
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

func (s Person) SetFirstname(v string) error {
	t, err := capnp.NewText(s.Struct.Segment(), v)
	if err != nil {
		return err
	}
	return s.Struct.SetPtr(0, t.List.ToPtr())
}

func (s Person) Lastname() (string, error) {
	p, err := s.Struct.Ptr(1)
	if err != nil {
		return "", err
	}
	return p.Text(), nil
}

func (s Person) HasLastname() bool {
	p, err := s.Struct.Ptr(1)
	return p.IsValid() || err != nil
}

func (s Person) LastnameBytes() ([]byte, error) {
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

func (s Person) SetLastname(v string) error {
	t, err := capnp.NewText(s.Struct.Segment(), v)
	if err != nil {
		return err
	}
	return s.Struct.SetPtr(1, t.List.ToPtr())
}

func (s Person) Dob() (Date, error) {
	p, err := s.Struct.Ptr(2)
	if err != nil {
		return Date{}, err
	}
	return Date{Struct: p.Struct()}, nil
}

func (s Person) HasDob() bool {
	p, err := s.Struct.Ptr(2)
	return p.IsValid() || err != nil
}

func (s Person) SetDob(v Date) error {
	return s.Struct.SetPtr(2, v.Struct.ToPtr())
}

// NewDob sets the dob field to a newly
// allocated Date struct, preferring placement in s's segment.
func (s Person) NewDob() (Date, error) {
	ss, err := NewDate(s.Struct.Segment())
	if err != nil {
		return Date{}, err
	}
	err = s.Struct.SetPtr(2, ss.Struct.ToPtr())
	return ss, err
}

func (s Person) Email() (string, error) {
	p, err := s.Struct.Ptr(3)
	if err != nil {
		return "", err
	}
	return p.Text(), nil
}

func (s Person) HasEmail() bool {
	p, err := s.Struct.Ptr(3)
	return p.IsValid() || err != nil
}

func (s Person) EmailBytes() ([]byte, error) {
	p, err := s.Struct.Ptr(3)
	if err != nil {
		return nil, err
	}
	d := p.Data()
	if len(d) == 0 {
		return d, nil
	}
	return d[:len(d)-1], nil
}

func (s Person) SetEmail(v string) error {
	t, err := capnp.NewText(s.Struct.Segment(), v)
	if err != nil {
		return err
	}
	return s.Struct.SetPtr(3, t.List.ToPtr())
}

func (s Person) Phones() (Person_PhoneNumber_List, error) {
	p, err := s.Struct.Ptr(4)
	if err != nil {
		return Person_PhoneNumber_List{}, err
	}
	return Person_PhoneNumber_List{List: p.List()}, nil
}

func (s Person) HasPhones() bool {
	p, err := s.Struct.Ptr(4)
	return p.IsValid() || err != nil
}

func (s Person) SetPhones(v Person_PhoneNumber_List) error {
	return s.Struct.SetPtr(4, v.List.ToPtr())
}

// NewPhones sets the phones field to a newly
// allocated Person_PhoneNumber_List, preferring placement in s's segment.
func (s Person) NewPhones(n int32) (Person_PhoneNumber_List, error) {
	l, err := NewPerson_PhoneNumber_List(s.Struct.Segment(), n)
	if err != nil {
		return Person_PhoneNumber_List{}, err
	}
	err = s.Struct.SetPtr(4, l.List.ToPtr())
	return l, err
}

// Person_List is a list of Person.
type Person_List struct{ capnp.List }

// NewPerson creates a new list of Person.
func NewPerson_List(s *capnp.Segment, sz int32) (Person_List, error) {
	l, err := capnp.NewCompositeList(s, capnp.ObjectSize{DataSize: 0, PointerCount: 5}, sz)
	if err != nil {
		return Person_List{}, err
	}
	return Person_List{l}, nil
}

func (s Person_List) At(i int) Person           { return Person{s.List.Struct(i)} }
func (s Person_List) Set(i int, v Person) error { return s.List.SetStruct(i, v.Struct) }

// Person_Promise is a wrapper for a Person promised by a client call.
type Person_Promise struct{ *capnp.Pipeline }

func (p Person_Promise) Struct() (Person, error) {
	s, err := p.Pipeline.Struct()
	return Person{s}, err
}

func (p Person_Promise) Dob() Date_Promise {
	return Date_Promise{Pipeline: p.Pipeline.GetPipeline(2)}
}

type Person_PhoneNumber struct{ capnp.Struct }

func NewPerson_PhoneNumber(s *capnp.Segment) (Person_PhoneNumber, error) {
	st, err := capnp.NewStruct(s, capnp.ObjectSize{DataSize: 8, PointerCount: 1})
	if err != nil {
		return Person_PhoneNumber{}, err
	}
	return Person_PhoneNumber{st}, nil
}

func NewRootPerson_PhoneNumber(s *capnp.Segment) (Person_PhoneNumber, error) {
	st, err := capnp.NewRootStruct(s, capnp.ObjectSize{DataSize: 8, PointerCount: 1})
	if err != nil {
		return Person_PhoneNumber{}, err
	}
	return Person_PhoneNumber{st}, nil
}

func ReadRootPerson_PhoneNumber(msg *capnp.Message) (Person_PhoneNumber, error) {
	root, err := msg.RootPtr()
	if err != nil {
		return Person_PhoneNumber{}, err
	}
	return Person_PhoneNumber{root.Struct()}, nil
}
func (s Person_PhoneNumber) Number() (string, error) {
	p, err := s.Struct.Ptr(0)
	if err != nil {
		return "", err
	}
	return p.Text(), nil
}

func (s Person_PhoneNumber) HasNumber() bool {
	p, err := s.Struct.Ptr(0)
	return p.IsValid() || err != nil
}

func (s Person_PhoneNumber) NumberBytes() ([]byte, error) {
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

func (s Person_PhoneNumber) SetNumber(v string) error {
	t, err := capnp.NewText(s.Struct.Segment(), v)
	if err != nil {
		return err
	}
	return s.Struct.SetPtr(0, t.List.ToPtr())
}

func (s Person_PhoneNumber) Type() Person_PhoneNumber_Type {
	return Person_PhoneNumber_Type(s.Struct.Uint16(0))
}

func (s Person_PhoneNumber) SetType(v Person_PhoneNumber_Type) {
	s.Struct.SetUint16(0, uint16(v))
}

// Person_PhoneNumber_List is a list of Person_PhoneNumber.
type Person_PhoneNumber_List struct{ capnp.List }

// NewPerson_PhoneNumber creates a new list of Person_PhoneNumber.
func NewPerson_PhoneNumber_List(s *capnp.Segment, sz int32) (Person_PhoneNumber_List, error) {
	l, err := capnp.NewCompositeList(s, capnp.ObjectSize{DataSize: 8, PointerCount: 1}, sz)
	if err != nil {
		return Person_PhoneNumber_List{}, err
	}
	return Person_PhoneNumber_List{l}, nil
}

func (s Person_PhoneNumber_List) At(i int) Person_PhoneNumber {
	return Person_PhoneNumber{s.List.Struct(i)}
}
func (s Person_PhoneNumber_List) Set(i int, v Person_PhoneNumber) error {
	return s.List.SetStruct(i, v.Struct)
}

// Person_PhoneNumber_Promise is a wrapper for a Person_PhoneNumber promised by a client call.
type Person_PhoneNumber_Promise struct{ *capnp.Pipeline }

func (p Person_PhoneNumber_Promise) Struct() (Person_PhoneNumber, error) {
	s, err := p.Pipeline.Struct()
	return Person_PhoneNumber{s}, err
}

type Person_PhoneNumber_Type uint16

// Values of Person_PhoneNumber_Type.
const (
	Person_PhoneNumber_Type_mobile Person_PhoneNumber_Type = 0
	Person_PhoneNumber_Type_home   Person_PhoneNumber_Type = 1
	Person_PhoneNumber_Type_work   Person_PhoneNumber_Type = 2
)

// String returns the enum's constant name.
func (c Person_PhoneNumber_Type) String() string {
	switch c {
	case Person_PhoneNumber_Type_mobile:
		return "mobile"
	case Person_PhoneNumber_Type_home:
		return "home"
	case Person_PhoneNumber_Type_work:
		return "work"

	default:
		return ""
	}
}

// Person_PhoneNumber_TypeFromString returns the enum value with a name,
// or the zero value if there's no such value.
func Person_PhoneNumber_TypeFromString(c string) Person_PhoneNumber_Type {
	switch c {
	case "mobile":
		return Person_PhoneNumber_Type_mobile
	case "home":
		return Person_PhoneNumber_Type_home
	case "work":
		return Person_PhoneNumber_Type_work

	default:
		return 0
	}
}

type Person_PhoneNumber_Type_List struct{ capnp.List }

func NewPerson_PhoneNumber_Type_List(s *capnp.Segment, sz int32) (Person_PhoneNumber_Type_List, error) {
	l, err := capnp.NewUInt16List(s, sz)
	if err != nil {
		return Person_PhoneNumber_Type_List{}, err
	}
	return Person_PhoneNumber_Type_List{l.List}, nil
}

func (l Person_PhoneNumber_Type_List) At(i int) Person_PhoneNumber_Type {
	ul := capnp.UInt16List{List: l.List}
	return Person_PhoneNumber_Type(ul.At(i))
}

func (l Person_PhoneNumber_Type_List) Set(i int, v Person_PhoneNumber_Type) {
	ul := capnp.UInt16List{List: l.List}
	ul.Set(i, uint16(v))
}
