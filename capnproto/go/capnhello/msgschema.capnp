using Go = import "../../zombiezen/go-capnproto2/go.capnp";
@0x85d3acc39d94e0f8;
$Go.package("data");
$Go.import("data/messages");

struct Message {
    id @0 : Int64;
    subject @1 :Text;
    body @2: Text;
}