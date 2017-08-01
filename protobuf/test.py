from js9 import j


print(j.application.getMemoryUsage())


import addressbook_pb2
# import leveldb


person = addressbook_pb2.Person()
#
# db = leveldb.LevelDB('./db')
#
res = []
for i in range(1000):
    person.name = "thisname%s" % i
    person.id = i
    person.email = "thisemail.%s.com" % i
    for t in range(3):
        phone = person.phones.add()
        phone.number = "324754064%s" % t
    data = person.SerializeToString()

    # key = "person.%s" % i

    res.append(data)

    # db.Put(key.encode(), data)
#
#
# from IPython import embed
# print("DEBUG NOW 87")
# embed()
# raise RuntimeError("stop debug here")
print(j.application.getMemoryUsage())
