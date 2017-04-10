from JumpScale import j


ActionMethodDecorator=j.atyourservice.getActionMethodDecorator()
ActionsBaseMgmt=j.atyourservice.getActionsBaseClassMgmt()

class action(ActionMethodDecorator):
    def __init__(self,*args,**kwargs):
        ActionMethodDecorator.__init__(self,*args,**kwargs)







class Actions(ActionsBaseMgmt):

    

    @action()
    def init(self,service):

        config="""
        github.label.priority.critical: ['*']
        github.label.priority.minor: ['*']
        github.label.priority.normal: ['*']
        github.label.priority.urgent: ['*']
        github.label.process.duplicate: ['*']
        github.label.process.wontfix: ['*']
        github.label.state.inprogress: ['*']
        github.label.state.question: ['*']
        github.label.state.verification: ['*']
        github.label.type.bug: [code, ays, cockpit, doc, www]
        github.label.type.feature: [code, ays, cockpit, doc, www]
        github.label.type.monitor: [proj, www, cockpit]
        github.label.type.assistance_request: [proj]
        github.label.type.question: [home, code, proj, ays, doc, cockpit, www,milestone,org]
        github.label.type.story: [home, proj, milestone,org]
        github.label.type.task: [home,milestone,proj,org]
        github.label.type.ticket: [proj,org]
        github.label.type.lead: [proj,org]
        github.project.types: [home, proj, cockpit, doc, ays, code, www, milestone,org]
        """


        j.data.text.strip(config)

        labels=j.data.serializer.yaml.loads(config)

        service.hrdCreate()
        service.hrd.setArgs(labels)


    @action()
    def install(self,service):
        return True

    def input(self,service,name,role,instance,serviceargs):
        return serviceargs


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
