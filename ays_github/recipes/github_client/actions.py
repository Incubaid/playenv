from JumpScale import j


ActionMethodDecorator=j.atyourservice.getActionMethodDecorator()
ActionsBaseMgmt=j.atyourservice.getActionsBaseClassMgmt()

class action(ActionMethodDecorator):
    def __init__(self,*args,**kwargs):
        ActionMethodDecorator.__init__(self,*args,**kwargs)




class Actions(ActionsBaseMgmt):


    @action()
    def install(self,service):
        self.monitor(service=service)


    @action()
    def monitor(self,service):
        g=self.getGithubClient(service=service)
        #@todo implement test

    def getGithubClient(self,service):
        g=j.clients.github.getClient(service.hrd.get("github.secret"))        
        return g

    @action()
    def test(self,service):
        print ("test")

    @action()
    def test2(self,service):
        print ("test2")        
        print ("$(github.secret)")        

    @action(queue="main")
    def testasync(self,service):
        print ("testasync")        
        print ("$(github.secret)")                

    def input(self,service,name,role,instance,serviceargs):
        return serviceargs


    @action()
    def init(self,service):
        return True


    @action()
    def stop(self,service):
        return True


    @action()
    def start(self,service):
        return True


    @action()
    def halt(self,service):
        return True


    @action()
    def check_up(self,service):
        return True


    @action()
    def check_down(self,service):
        return True


    @action()
    def check_requirements(self,service):
        return True


    @action()
    def cleanup(self,service):
        return True


    @action()
    def data_export(self,service):
        return True


    @action()
    def data_import(self,service):
        return True


    @action()
    def uninstall(self,service):
        return True


    @action()
    def removedata(self,service):
        return True
