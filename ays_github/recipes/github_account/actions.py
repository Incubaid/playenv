from JumpScale import j


ActionMethodDecorator=j.atyourservice.getActionMethodDecorator()
ActionsBaseMgmt=j.atyourservice.getActionsBaseClassMgmt()

class action(ActionMethodDecorator):
    def __init__(self,*args,**kwargs):
        ActionMethodDecorator.__init__(self,*args,**kwargs)



class Actions(ActionsBaseMgmt):


    def input(self,service,name,role,instance,serviceargs):
        return serviceargs


    @action()
    def init(self,service):
        return True


    @action()
    def install(self,service):
        return True


    @action()
    def stop(self,service):
        return True


    @action()
    def start(self,service):
        return True


    @action()
    def monitor(self,service):
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
