using Go = import "../../zombiezen/go-capnproto2/go.capnp";
@0x85d3acc39d94e0f8;
$Go.package("data");
$Go.import("data/books");

struct Book {
    id @0 : Int64;
    title @1 :Text;
    author @2: Text;
}