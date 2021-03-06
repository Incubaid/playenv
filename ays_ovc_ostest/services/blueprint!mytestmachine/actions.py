
from JumpScale import j
ActionMethodDecorator=j.atyourservice.getActionMethodDecorator()
class actionmethod(ActionMethodDecorator):
    def __init__(self,*args,**kwargs):
        ActionMethodDecorator.__init__(self,*args,**kwargs)
        self.selfobjCode="service=j.atyourservice.getService(role='blueprint', instance='mytestmachine', die=True);selfobj=service.actions;selfobj.service=service"
class Actions():

    @actionmethod()
    def init(self):
        
        args=self.service.args

        if 'g8.url' in args:
            #will use existing one if it exists
            j.atyourservice.new('g8client', args=args, instance="main")

        # args = {
        #     'url': 'https://dns1.aydo.com/etcd',
        #     'login': '$(dns.login)',
        #     'password': '$(dns.password)'
        # }
        # dns_client = j.atyourservice.new('dns_client', args=args, instance="main")


        sshkey = j.atyourservice.new('sshkey', instance="main")

        if "vdc.farm" in args:
            farminstance=args["vdc.farm"]
        else:
            farminstance="main"

        if "vdc.name" in args:
            vdcname=args["vdc.name"]
        else:
            vdcname="main"

        vdcfarm = j.atyourservice.new('vdcfarm', instance=farminstance)

        vdc = j.atyourservice.new('vdc',instance=vdcname, parent=vdcfarm)

        from IPython import embed
        print ("DEBUG NOW blueprint os")
        embed()
        

        args = {'ports': '80:80, 443:443, 18384:18384'}
        node_ovc = j.atyourservice.new('node.ovc', args=args, instance="cockpitvm", parent=vdc)

        args = {'node': node_ovc.instance}
        os = j.atyourservice.new('os.ssh.ubuntu', args=args, instance=self.service.instance, parent=node_ovc)

    def input(self,name,role,instance,serviceargs):
        return serviceargs


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

