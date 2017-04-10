

class Actions():


    def hrd(self):
        sshkey = j.atyourservice.getService(role='sshkey', instance=self.service.hrd.getStr('sshkey'))
        self.service.hrd.set("ssh.key.public", sshkey.hrd.get("key.pub"))
        self.service.hrd.set("ssh.key.private", sshkey.hrd.get("key.priv"))

        if self.service.hrd.get("system.backdoor.passwd").strip() == "":
            self.service.hrd.set("system.backdoor.passwd", j.data.idgenerator.generateXCharID(12))
        return True

    #def consume(self, producer):
    #    if producer.role == 'sshkey':
    #        self.service.hrd.set("ssh.key.public", producer.hrd.get("key.pub"))


    
    def install_enableAccess(self):
        # pub = self.service.hrd.get("ssh.key.public")
        from IPython import embed
        print ("DEBUG NOW install_enableAccess, need to retrieve keys from consumers")
        embed()
        
        self._cuisine.ssh.enableAccess(keys,"$(system.backdoor.passwd)",backdoorlogin="$(system.backdoor.login)")


    def install_js8(self):
        if self.service.hrd.getBool('jumpscale.install', default=False):
            if self.service.hrd.getBool("jumpscale.sandbox")==True:
                self.cusine.install.jumpscale8(rw=self.service.hrd.getBool("jumpscale.sandbox.rw"))
            else:
                self.cusine.installdevelop.jumpscale8()

    def install(self):
        self.install_enableAccess()
        self.install_js8()

    
    @property
    def cuisine(self):
        """
        @rvalue ssh client object connected to the node
        """
        port = int(self.service.hrd.get("ssh.port"))
        executor = j.tools.executor.getSSHBased(addr="$(node.tcp.addr)", port=port, login='root')
        return executor.cuisine

    def reset(self):
        # create the backdoor user, make sure is always done, we don't want to be locked out
        self.createbackdoor(self.service)
