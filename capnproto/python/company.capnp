# company.capnp
@0xc8c7b2b541f192ce;

const qux :UInt32 = 123;

struct Branch {
  id @0 :UInt32;
  name @1 :Text;
  email @2 :Text;
  phones @3 :List(PhoneNumber);
  struct PhoneNumber {
    number @0 :Text;
    type @1 :Type;

    enum Type {
      land @0;
      mobile @1;
    }
  }

  field @4 : Field;
  enum Field {
      head @0;
      development @1;
    }

  address @5 :Text;

}

struct Company {
  branches @0 :List(Branch);
  name @1: Text;
}

