from JumpScale import j

class Actions():
    def init(self):
        # test ssh connection
        host = self.service.hrd.get("ssh")
        s = j.tools.cuisine.get(j.tools.executor.getSSHBased(addr=host))
        

    def install(self):
        """
        Deploy and run a drupal website
        """
        host = self.service.hrd.get("ssh")
        c = j.tools.cuisine.get(j.tools.executor.getSSHBased(addr=host))
        
        c.docker.install()
