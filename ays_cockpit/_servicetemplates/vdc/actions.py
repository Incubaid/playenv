
from JumpScale import j


class Actions():

    def getClient(self):
        return self.service.parent.action_methods_mgmt.getClient()

    def hrd(self):
        cloudspace = "$(vdcname)"
        if cloudspace.strip() == "":
            cloudspace = self.service.instance
            self.service.hrd.set("vdcname", cloudspace)

    def install(self):
        client = self.getClient()
        accountname = self.service.parent.hrd.get('account')
        account = client.account_get(accountname)
        account.space_get(self.service.instance, location='$(location)')
