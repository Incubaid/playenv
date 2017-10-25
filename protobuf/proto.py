from js9 import j
import blist
from blist import *  # https://github.com/DanielStutzbach/blist
from test_pb2 import *
from google.protobuf import json_format
from google.protobuf import text_format


class Person2():
    def __init__(self, nr):
        self.nr = nr

    @property
    def obj(self):
        m = Person()
        m.FromString(out[self.nr])
        return m


startmb = j.application.getMemoryUsage() / 1024
print("start:%s MB" % startmb)
print("start")
tot = 20000
data = "a" * 100
out = blist()
out2 = blist()
persons = []
for i in range(tot):
    m = Person()
    m.name = data
    m.phones.add(number="23424324", type=Person.MOBILE)
    m.SerializeToString()
    out.append(m.SerializeToString())
    out2.append("this is a name;urgent;something")
    # persons.append(Person2(i))
print("read")
for item in out:
    m = Person()
    m = m.FromString(item)
    json_format.MessageToDict(m)
    # text_format.MessageToString(m)
print("stop")


print("minsize:%s MB" % ((tot * (len(data) + 30)) / 1024 / 1024))

stopmb = j.application.getMemoryUsage() / 1024
print("dataused:%s MB" % (stopmb - startmb))

# res = []

# startmb = j.application.getMemoryUsage() / 1024
# print("start:%s MB" % startmb)
# print("start")
# tot = 100000
# data = "a" * 100
# for i in range(tot):
#     m = test.SearchRequest()
#     m.query = data
#     res.append(m)
# print("stop")

# print("minsize:%s MB" % (tot * len(data) / 1024 / 1024))

# stopmb = j.application.getMemoryUsage() / 1024
# print("dataused:%s MB" % (stopmb - startmb))
