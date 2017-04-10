

class Actions():

    def getClient(self):
        openvcloudClient = j.clients.openvcloud.get('$(apiurl)', '$(login)', '$(passwd)')
        return openvcloudClient
