from JumpScale import j


class Actions():

    def hrd(self):
        from IPython import embed
        print ("DEBUG NOW hrd host blueprint")
        embed()
        

        '''
        jumpscale.branch               = type:str default:'master'
        jumpscale.install              = type:bool default:true descr:'do you want to install jumpscale' @ASK
        jumpscale.sandbox              = type:bool default:true  
        jumpscale.sandbox.rw           = type:bool default:true  

        node.tcp.addr                  = type:str descr:'ipaddress of ssh node' @ASK
        ssh.port                       = type:str default:22

        system.backdoor.login          = type:str default:'backdoor'
        system.backdoor.passwd         = type:str @ASK
        install.seedpasswd             = type:str @ASK

        node                           = type:str parent:node parentauto
        sshkeys                        = type:str list consume:sshkey:5 

        '''