import os
import sys
from mylist import *
from collections import namedtuple

class myvm_bad_state_change(Exception):
    def __init__(self, vm, newstate, message="Active VMs are present"):
        self.vm=vm
        self.newstate=newstate
        self.oldstate=self.vm.state
        self.message=message
    def __str__(self):
        return f'{self.vm.name} oldstate: {self.oldstate} newstate: {self.newstate} bound to: {self.vm.sr} -> {self.message}'


# Creating Immutable Objects for V Conf
vconf=namedtuple('vc',['name','mem','ncpu'])
        
# This object implements the relevant operations/sate for the workings described
# in the mycrm object above. It will maintain the stats in the stats object sent
# in the init. Do not change the signature of the init class. You can add any
# more members you want other than what is listed.

# states:
#
# 'idle' :  not bound to any server. Happens when a server has failed. need to be
# reprovisioned only via mycrm.provision_all_idle_vms() or
# mycrm.provision_idle_vms(server) function. the idle vm being bound to a server
# does not go through the same provision, commit, undo etc. it is an internally
# managed operation by the mycrm.
#
# 'provision': in this state it is bound to a server, but not fully committed.
# It is a simple transition state until a commit or undo happens. undo deletes
# this vm, commit moves the vm to active state.
#
# 'active' : bound to a  server . happens when a commit is called on a
# provisioned 'vm' or when an idle vm is bound again to a server. 
# 'idle' --> active OR 'provision' --> active 
#
# 'deleted' : finally deleted but object will cease to exist after this.
# deprovision_vm will trigger this.

class myvm():

    # DO NOT change the init signature.
    # DO not change the members here. You are welcome to add more. But the
    # members described here has to be maintained, including the stats otherwise
    # Else all tests will fail and it wont be graded.
    # self.vc -->  a vconf immutable tuple that stores name, cpu and mem of this
    # vm.
    # self.amem, and self.acpu --> will be same as vc.mem and vc.ncpu and it
    # wont change during the life of this object for this assignment.
    # self.sr --> stores the bound server object.
    # self.stats--> where all the book keeping happens,. Have to be done
    # correctly.
    # self.state can be 'provision', 'idle', 'active'    when it is 'deleted'
    # the object will cease to exist.

    def __init__(self,vc,sr,stats):
        self.amem=vc.mem
        self.acpu=vc.ncpu
        self.name=vc.name
        self.state="provision"
        self.sr=sr
        self.stats=stats
        self.stats['vprovision'] +=1
        self.stats['vtotal'] += 1
        self.vc=vc

    # called during commit  by myserver object.
    # Set the vm state to active and do the accounting if 
    # the conditions for transiting to active state is met.
    # raise exceptions otherwise.
    # a vm can move to 'active' state from 'provision' state or 'idle' state.
    # do the book keeping on the self.stats right way.
    # self.sr should be set to sr to indicate it is bounded.

    def set_active(self, sr):
        if (self.state=='provision')|(self.state=='idle'):
            if self.state=='idle':
                self.stats['vidle']-=1
            else:
                self.stats['vprovision']-=1
                
            self.stats['vactive']+=1
            self.state='active'
            self.sr=sr
        else:
            raise myvm_bad_state_change(self,'active')
            

    #  called by myserver when it goes to fail state.
    #  unbound the server by setting self.sr = None.
    #  vm can move to idle state only from 'active' state.
    #  do the book keeping in self.stats

    def set_idle(self, sr):
        for virtual_machine in sr.vl:
            if (virtual_machine.state=='active') :
                virtual_machine.state='idle'
                virtual_machine.stats['vidle']+=1
                virtual_machine.stats['vactive']-=1
                virtual_machine.set_sr=None
            else:
                raise myvm_bad_state_change(self,'idle')
        sr.state='idle' # Since all the Virtual machines are now made idle, the Server will also become idle
        
        
    # called by mycrm.delete_vm() routine to delete
    # this vm OR by mycrm.provision_undo() routine after deprovisioning it
    # from server OR if it was already 'idle'.
    # hence vm state can be 'active' or 'provision' or 'idle' state and when 
    #  deleted the object is "deleted" state.after which there should not be 
    # any references any where and no one can refer to it.

    def delete(self, sr):
        if (self.state=='provision')|(self.state=='idle')|(self.state=='active'):         
            if self.state=='active':
                self.stats['vactive']-=1
            else:
                self.stats['vprovision']-=1
            
            self.state='deleted'
            self.sr=None
            self.stats['vtotal']-=1
            self.stats['vdeleted']+=1
            sr.vl.delete(self)
        else:
            raise myvm_bad_state_change(self,'delete')

    
    def __str__(self):
        return f'VM Name: {self.vc.name} \nVM memory : {self.amem} \nVM CPU: {self.acpu} \nVM State: {self.state}\nBound Server: \n{self.sr}\n\n'