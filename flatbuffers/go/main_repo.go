package main

import "fmt"
import "github.com/xmonader/flabtut/repo"
import "github.com/google/flatbuffers/go"

func pack() []byte {
	b:=&flatbuffers.Builder{}
    namepos:=b.CreateString("A")
    reponame:=b.CreateString("simpleproj")
    f1:=b.CreateString("t1")
    f2:=b.CreateString("t2")
    
    repo.RepoStartFilesVector(b, 2)
    b.PrependUOffsetT(f1)
    b.PrependUOffsetT(f2)
    fs:=b.EndVector(2)
    
    repo.UserInfoStart(b)
    repo.UserInfoAddId(b, 1)
    repo.UserInfoAddName(b, namepos)
    repo.UserInfoEnd(b)
    
    repo.RepoStart(b)
    repo.RepoAddId(b, 1)
    repo.RepoAddName(b, reponame)
    repo.RepoAddLanguage(b, repo.LangGo)
    
    repo.RepoAddFiles(b, fs)
  
	reppos:=repo.RepoEnd(b)
	b.Finish(reppos)
	return b.Bytes[b.Head():]
}
func read(buf []byte) {
	r:=repo.GetRootAsRepo(buf, 0)
    fmt.Println("REPO: ", r.Id(), r.Language(), string(r.Name()), string(r.Files(0)))
}
func main() {
	read(pack())
}
