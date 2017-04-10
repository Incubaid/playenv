package main

import "fmt"
import (
	"bytes"
	"github.com/xmonader/capnhello/data"
	"zombiezen.com/go/capnproto2"
)

func dumpprogrammer() *bytes.Buffer {
	buf := new(bytes.Buffer)
	msg, seg, err := capnp.NewMessage(capnp.SingleSegment(nil))
	if err != nil {
		panic(err)
	}
	p, _ := data.NewRootProgrammer(seg)

	p.SetName("ahmed")
	p.SetEmail("ahmed@there.com")
	likes, _ := p.NewLikes(3)
	likes.Set(0, "python")
	likes.Set(1, "haskell")
	likes.Set(2, "go")
	p.SetLikes(likes)

	err = capnp.NewEncoder(buf).Encode(msg)
	if err != nil {
		panic(err)
	}
	return buf
}
func loadprogrammer(buf *bytes.Buffer) {

	d, err := capnp.NewDecoder(buf).Decode()
	if err != nil {
		panic(err)
	}
	p, err := data.ReadRootProgrammer(d)
	if err != nil {
		panic(err)
	}
	fmt.Println(p)
}

func dumpperson() *bytes.Buffer {
	buf := new(bytes.Buffer)
	msg, seg, err := capnp.NewMessage(capnp.SingleSegment(nil))
	if err != nil {
		panic(err)
	}
	p, err := data.NewRootPerson(seg)
	if err != nil {
		panic(err)
	}
	p.SetFirstname("First name")
	p.SetLastname("Last name")
	date, err := data.NewDate(seg)
	if err != nil {
		panic(err)
	}
	date.SetMonth(9)
	date.SetDay(3)
	date.SetYear(1929)
	p.SetDob(date)
	p.SetEmail("someone@there")
	phones, err := p.NewPhones(2)
	if err != nil {
		panic(err)
	}
	n1, err := data.NewPerson_PhoneNumber(seg)
	if err != nil {
		panic(err)
	}
	n1.SetNumber("3312321")
	n1.SetType(data.Person_PhoneNumber_Type_home)
	n2, err := data.NewPerson_PhoneNumber(seg)
	if err != nil {
		panic(err)
	}
	n1.SetNumber("4444444")
	n2.SetType(data.Person_PhoneNumber_Type_mobile)
	phones.Set(0, n1)
	phones.Set(1, n2)
	p.SetPhones(phones)

	first, _ := p.Firstname()
	last, _ := p.Lastname()
	email, _ := p.Email()
	dob, _ := p.Dob()

	phs, _ := p.Phones()
	fmt.Println(first, last, email, dob, phs)
	//fmt.Printf("%v\n", p)

	err = capnp.NewEncoder(buf).Encode(msg)
	if err != nil {
		panic(err)
	}
	//fmt.Println(buf)
	return buf
}
func loadperson(buf *bytes.Buffer) {
	fmt.Println(buf)
	d, err := capnp.NewDecoder(buf).Decode()
	if err != nil {
		panic(err)
	}
	//fmt.Println(d)

	p, err := data.ReadRootPerson(d)

	if err != nil {
		panic(err)
	}
	fmt.Printf("person: %v \n", p)

	first, err := p.Firstname()
	if err != nil {
		panic(err)
	}
	last, err := p.Lastname()
	if err != nil {
		panic(err)
	}

	email, err := p.Email()
	if err != nil {
		panic(err)
	}
	dob, err := p.Dob()
	if err != nil {
		panic(err)
	}
	phones, err := p.Phones()
	if err != nil {
		panic(err)
	}
	fmt.Println(first, last, email, dob, phones)

}
func dumpbook() *bytes.Buffer {
	buf := new(bytes.Buffer)
	msg, seg, err := capnp.NewMessage(capnp.SingleSegment(nil))
	if err != nil {
		panic(err)
	}
	b, _ := data.NewRootBook(seg)

	b.SetId(31)
	b.SetTitle("Fake title")
	b.SetAuthor("Fake author name")

	err = capnp.NewEncoder(buf).Encode(msg)
	if err != nil {
		panic(err)
	}
	return buf
}
func loadbook(buf *bytes.Buffer) {

	d, err := capnp.NewDecoder(buf).Decode()
	if err != nil {
		panic(err)
	}
	b, errx := data.ReadRootBook(d)
	if errx != nil {
		panic(errx)
	}
	id := b.Id()
	title, _ := b.Title()
	author, _ := b.Author()
	fmt.Println(id, title, author)
}
func dumpmessage() *bytes.Buffer {
	buf := new(bytes.Buffer)

	msg, seg, err := capnp.NewMessage(capnp.SingleSegment(nil))
	if err != nil {
		panic(err)
	}
	m, _ := data.NewRootMessage(seg)

	m.SetId(3)
	m.SetSubject("First subject")
	m.SetBody("This is the bodyyy")

	err = capnp.NewEncoder(buf).Encode(msg)
	if err != nil {
		panic(err)
	}
	return buf
}

func loadmessage(b *bytes.Buffer) {

	d, err := capnp.NewDecoder(b).Decode()
	if err != nil {
		panic(err)
	}
	m, err := data.ReadRootMessage(d)
	if err != nil {
		panic(err)
	}
	id := m.Id()
	sub, _ := m.Subject()
	bod, _ := m.Body()
	fmt.Println(id, sub, bod)
}
func main() {
	loadmessage(dumpmessage())
	loadbook(dumpbook())
	loadperson(dumpperson())
	loadprogrammer(dumpprogrammer())
}
