
from JumpScale import j
ActionMethodDecorator=j.atyourservice.getActionMethodDecorator()
class actionmethod(ActionMethodDecorator):
    def __init__(self,*args,**kwargs):
        ActionMethodDecorator.__init__(self,*args,**kwargs)
        self.selfobjCode="service=j.atyourservice.getService(role='sshkey', instance='main', die=True);selfobj=service.actions;selfobj.service=service"
class Actions():
    def _startAgent(self):
        # FIXME
        j.do.execute("ssh-agent", die=False, showout=False, outputStderr=False)
    def getSSHKey(self):
        keydest = j.sal.fs.joinPaths(self.service.path, "sshkey_%s"%self.service.instance)
        privkey = j.sal.fs.fileGetContents(keydest)
        pubkey = j.sal.fs.fileGetContents(keydest + ".pub")
        return privkey, pubkey

    @actionmethod()
    def init(self):
        """
        create key
        """
        if self.service.hrd.get("key.name") == "":
            self.service.hrd.set("key.name", self.service.instance)

        name=self.service.hrd.get("key.name") 
        
        tmpdir=j.sal.fs.getTmpDirPath()

        if j.do.getSSHKeyPathFromAgent(name, die=False)!=None:
            keyfile = j.do.getSSHKeyPathFromAgent(name)
        elif '' != "":
            keyfile = ''
        else:
            keyfile=j.sal.fs.joinPaths(tmpdir,name)
            cmd = "ssh-keygen -t rsa -f %s -P '%s' " % (keyfile, self.service.hrd.getStr('key.passphrase'))
            print(cmd)
            j.sal.process.executeWithoutPipe(cmd)

        if not j.sal.fs.exists(keyfile):
            raise j.exceptions.Input("Cannot find ssh key location:%s"%keyfile)

        keydest = j.sal.fs.joinPaths(self.service.path, "sshkey_%s"%self.service.instance)
        j.sal.fs.copyFile(keyfile,keydest)
        j.sal.fs.copyFile(keyfile+".pub",keydest+".pub")

        j.sal.fs.chmod(keydest, 0o600)
        j.sal.fs.chmod(keydest+".pub", 0o600)

        j.sal.fs.removeDir(tmpdir)

        self.install()

    @actionmethod()
    def install(self):
        j.do.loadSSHAgent()
        self.start()

    @actionmethod()
    def start(self):
        """
        Add key to SSH Agent if not already loaded
        """
        keypath=j.sal.fs.joinPaths(self.service.path, "sshkey_%s"%self.service.instance)
        j.do.loadSSHKeys(keypath)

    def input(self,name,role,instance,serviceargs):
        return serviceargs


    @actionmethod()
    def stop(self):
        return True


    @actionmethod()
    def monitor(self):
        return True


    @actionmethod()
    def halt(self):
        return True


    @actionmethod()
    def check_up(self):
        return True


    @actionmethod()
    def check_down(self):
        return True


    @actionmethod()
    def check_requirements(self):
        return True


    @actionmethod()
    def cleanup(self):
        return True


    @actionmethod()
    def data_export(self):
        return True


    @actionmethod()
    def data_import(self):
        return True


    @actionmethod()
    def uninstall(self):
        return True


    @actionmethod()
    def removedata(self):
        return True


    def change(self,stateitem):
        return True

