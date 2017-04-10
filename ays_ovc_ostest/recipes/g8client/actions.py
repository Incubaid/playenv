
from JumpScale import j
ActionMethodDecorator=j.atyourservice.getActionMethodDecorator()
class actionmethod(ActionMethodDecorator):
    def __init__(self,*args,**kwargs):
        ActionMethodDecorator.__init__(self,*args,**kwargs)
        self.selfobjCode="service=j.atyourservice.getService(role='$(service.role)', instance='$(service.instance)', die=True);selfobj=service.actions;selfobj.service=service"
class Actions():
    def getClient(self):
        """
        return client towards g8 master
        """
        return j.clients.openvcloud.get("$(g8.url)", '$(g8.login)', '$(g8.password)')

    @actionmethod()
    def init(self):
        pass
    def input(self,name,role,instance,args={}):

        if "g8.account" not in args or args["g8.account"].strip()=="":
            args['g8.account']=args["g8.login"]

        return args

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

