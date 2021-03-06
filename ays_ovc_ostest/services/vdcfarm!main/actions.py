
from JumpScale import j
ActionMethodDecorator=j.atyourservice.getActionMethodDecorator()
class actionmethod(ActionMethodDecorator):
    def __init__(self,*args,**kwargs):
        ActionMethodDecorator.__init__(self,*args,**kwargs)
        self.selfobjCode="service=j.atyourservice.getService(role='vdcfarm', instance='main', die=True);selfobj=service.actions;selfobj.service=service"
class Actions():

    def input(self,name,role,instance,serviceargs):
        return serviceargs


    @actionmethod()
    def init(self):
        return True


    @actionmethod()
    def install(self):
        return True


    @actionmethod()
    def stop(self):
        return True


    @actionmethod()
    def start(self):
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

