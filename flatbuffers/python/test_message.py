from data.Message import *
from flatbuffers import Builder

def packmsg():
    b=Builder(0)
    #create the fields first
    subj=b.CreateString("Hello")
    body=b.CreateString("This is the body")

    #start
    MessageStart(b)
    MessageAddId(b, 32)
    MessageAddSubject(b, subj)
    MessageAddBody(b, body)

    #End
    pos=MessageEnd(b)
    b.Finish(pos)
    return b.Output()

def readmsg(buf):
    m=Message.GetRootAsMessage(buf, 0)
    print(m.Id(), m.Subject(), m.Body())



if __name__=="__main__":
    readmsg(packmsg())
    #with open('message.dat', 'wb') as f:
    #    f.write(packmsg())
