from JumpScale import j


class Actions():

    def __init__(self, service):
        super(Actions, self).__init__(service)
        self._cuisine = None

    @property
    def cuisine(self):
        if self._cuisine is None:
            machine = self.getMachine()
            self.service.hrd.set("machine.id", machine.id)
            executor = machine.get_ssh_connection()
            addr = executor.addr
            port = executor.port
            self._cuisine = j.tools.executor.getSSHBased(addr, port).cuisine
        return self._cuisine

    def hrd(self):
        # def setDockerSize():
        #     size = self.service.hrd.getInt("docker.size")
        #     ok = [8]
        #     for item in ok:
        #         if item == size:
        #             self.service.hrd.set("docker.size", item)
        #             return
        #         if size < item:
        #             self.service.hrd.set("docker.size", item)
        #             return
        #     self.service.hrd.set("docker.size", item)

        def setDiskSize():
            size = self.service.hrd.getInt("disk.size")
            ok = [20]
            for item in ok:
                if item == size:
                    self.service.hrd.set("disk.size", item)
                    return
                if size < item:
                    self.service.hrd.set("disk.size", item)
                    return
            self.service.hrd.set("disk.size", item)

        # setDockerSize()
        setDiskSize()

    def getClient(self):
        vdc = self.service.parent
        client = vdc.action_methods_mgmt.getClient()
        return client

    def getSpace(self):
        vdc = self.service.parent
        farm = vdc.parent

        account = self.getClient().account_get(farm.hrd.get('account'))
        space = account.space_get(vdc.instance, location=vdc.hrd.get('location'))
        return space

    def getMachine(self):
        space = self.getSpace()

        if self.service.instance in space.machines:
            machine = space.machines[self.service.instance]
        else:
            machine = space.machine_create(name=self.service.instance,
                                           image='$(os.image)',
                                           memsize=int('$(os.size)'))
        return machine

    def install(self):
        machine = self.getMachine()
        executor = machine.get_ssh_connection()

        # expose weave
        if self.service.hrd.getBool('weave'):
            pf_existing = {'tcp': [], 'udp': []}
            for pf in machine.portforwardings:
                pf_existing[pf['protocol']].append(pf['publicPort'])
            print(pf_existing)

            if '6783' not in pf_existing['tcp']:
                machine.create_portforwarding('6783', '6783', 'tcp')
            if '6783' not in pf_existing['udp']:
                machine.create_portforwarding('6783', '6783', 'udp')
            if '6784' not in pf_existing['udp']:
                machine.create_portforwarding('6784', '6784', 'udp')

        self.service.hrd.set("machine.id", machine.id)
        self.service.hrd.set("machine.publicip", executor.addr)
        nics = machine.model['nics']
        if nics:
            privateip = nics[0]['ipAddress']
            self.service.hrd.set("machine.privateip", privateip)
        self.service.hrd.set("machine.sshport", executor.port)

        # authorize sshkey for root user
        executor.cuisine.set_sudomode()
        if 'sshkey' in self.service.producers:
            sshkey = self.service.producers['sshkey'][0]
            sshkey_pub = sshkey.hrd.get('key.pub')
        else:
            raise j.exceptions.RuntimeError("No sshkey found. please consume an sshkey service")
        print("authorize ssh key to machine")
        executor.cuisine.ssh.authorize('root', sshkey_pub)

        # reconnect as root
        executor = j.tools.executor.getSSHBased(executor.addr, executor.port, 'root')
        # executor.cuisine.core.run('apt-get update')
        if self.service.hrd.getBool("aysfs"):
            executor.cuisine.installer.jumpscale8(force=True)
        else:
            executor.cuisine.installerdevelop.jumpscale8(force=True)
        #    build core only if no aysfs
        #    if self.service.hrd.getBool('agent'):
        #        executor.cuisine.builder.core(j.application.whoAmI.gid, machine.id)

        # get gid from cockpit config
        # if self.service.hrd.getBool('agent'):
        #     executor.cuisine.builder._startCore(j.application.whoAmI.gid, machine.id)

    def uninstall(self):
        machine = self.getMachine()
        machine.stop()
        machine.delete()
