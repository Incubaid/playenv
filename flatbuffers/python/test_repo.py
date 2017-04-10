from repo.Lang import *
from repo.Repo import *
from repo.UserInfo import *
from flatbuffers import Builder

def packmsg():
    b=Builder(0)

    ##Init the fields first.
    namepos=b.CreateString("A")
    reponame=b.CreateString("simpleproj")
    f1=b.CreateString('t1')
    f2=b.CreateString('t2')

    RepoStartFilesVector(b, 2)
    b.PrependUOffsetTRelative(f1)
    b.PrependUOffsetTRelative(f2)
    fs=b.EndVector(2)


    UserInfoStart(b)
    UserInfoAddId(b, 1)
    UserInfoAddName(b, namepos)
    pos=UserInfoEnd(b)

    RepoStart(b)
    RepoAddId(b, 1)
    RepoAddName(b, reponame)
    RepoAddLanguage(b, Lang.Python)

    RepoAddFiles(b,fs)
    pos=RepoEnd(b)
    b.Finish(pos)
    return b.Output()

def readmsg(buf):
    r=Repo.GetRootAsRepo(buf, 0)
    print(r.Id(), r.Name(), r.Language(), r.Files(0), r.Files(1))



if __name__=="__main__":
    readmsg(packmsg())
