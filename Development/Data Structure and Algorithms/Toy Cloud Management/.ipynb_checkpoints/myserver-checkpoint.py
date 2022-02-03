import os
import sys
from mylist import *
from collections import namedtuple
from myvm import *

def vm_name_exists(Exception):
    def __init__(self,name):
        self.newname=name
    def __str__(self):
        return f'Server exists with name {self.newname}'
    
    
    
class myserver_activevms(Exception):
    def __init__(self, server, message="Active VMs are present"):
        self.server=server
        self.message=message
    def __str__(self):
        return f'{self.server} -> {self.message}'

class myserver_bad_state_change(Exception):
    def __init__(self, server, newstate, message="Active VMs are present"):
        self.server=server
        self.newstate=newstate
        self.message=message
    def __str__(self):
        return f'{self.server.name} oldstate: {self.server.state} newstate: {self.newstate} vmsactive: {self.server.nvms} -> {self.message}'

    
# Sconf object with details about the server like the name, memory needed and the cpu needed
    
class sconf:

    def __init__(self,name,mem,ncpu):
        self.mem=mem
        self.ncpu=ncpu
        self.name=name

    def __str__(self):
        return f'Server_Name: {self.name} Server_Memory: {self.memory} Server_CPU: {self.ncpu}'

# This object implements the relevant operations/sate for the workings described
# in the mycrm object above. It will maintain the stats in the stats object sent
# in the init. Do not change the signature of the init class. You can add any
# more members you want other than what is listed.

# states:
# 'idle' : ready to accept vm's and can have vms in 'provision' state bound to
# it.
# 'active' : ready to accept vm's and should have atleast one vm in 'active'
# state and other vms can be in either 'active' or in 'provision' state.
#
# 'fail' : can be failed and go to this state if there are no vms bound to it.
#
# 'deleted' : finally deleted but object will cease to exist after this.
sconf = namedtuple('sconf', 'name ncpu mem ')
vconf = namedtuple('vconf', 'name ncpu mem ')

class myserver():

    # DO NOT change the init signature.
    # DO not change the members here. You are welcome to add more. But the
    # members described here has to be maintained, including the stats otherwise
    # Else all tests will fail and it wont be graded.

    # self.sc -- sconf named tuple sent as part of creation. just contains the
    # immutable name, ncpu and memory of this server.
    # self.amem -- store the remaining available memory after whatever vms have
    # been provisioned to this. 
    # self.acpu -- store the remaining available cpus after whatever has been
    # self.nvms -- no. of vms that are bound to this, which could be in
    # 'provision' state or in 'active' state.
    # taken by the vms provisioned to this. 
    # [[ for eg., if server has 4 cpus, and 4G memory and two vms each took 1
    # cpu and 1G for itself, then then self.acpu=2,self.amem=2
    # self.state -- will be 'idle', 'active', or 'fail'. as explained below.
    # do the proper state transitions modify this and also do the accounting.
    # use whatever list data structures you need to accomplish this project.
    #vl : List of all virtual machines bound to the server

        
    def __init__(self,sc, stats):
        self.sc=sc
        self.amem=sc.mem
        self.acpu=sc.ncpu
        self.name=sc.name
        self.state='idle'
        self.nvms=0
        self.vl=mylist("list")
        self.stats=stats
        self.stats['sidle'] += 1
        self.stats['stotal'] += 1
        
    def __str__(self):
        return f'Server Name: {self.sc.name} \nServer memory : {self.amem} \nServer CPU: {self.acpu} \nServer State: {self.state}\nVirtual Machines: {self.nvms}'

# The following list of functions is just a guideline for you to think through
# the implementation and gain more insight. Except for the get_vms() function
# and the members listed above . 

    # Set the server state to fail and do the accounting if 
    # the conditions for transiting to fail state is met.
    # raise exceptions otherwise.

    def set_fail(self):
        if (self.state=='active') | (self.state=='idle'):
            if self.state=='active':
                self.stats['sactive']-=1
                
            else:
                self.stats['sidle']-=1
#             myvm.set_idle(self) # make all the servers idle in crm
            self.state='fail'
            self.stats['sfail']+=1
        else:
            
            raise myserver_bad_state_change(self,'fail')
            
            
    # Set the server state to active and do the accounting if 
    # the conditions for transiting to active state is met.
    # raise exceptions otherwise.

    def set_active(self):
        if self.state=='idle':
            self.state['sidle']-=1
            self.state['sactive']+=1
            self.state='active'
        else:
            raise myserver_bad_state_change(self,'active')

    # check if the server can provision this ie. check if the vconf object vc
    # ncpu, and mem can be allocated by this server given its current self.acpu
    # and self.amem value.
    # return "vc" object if success, else, return None.
    # no state transitions should take place here, as the provisioning
    # process has not commited yet.

    def can_provision(self,vc):
        unable=0
        if (self.state=='idle') | (self.state=='active'):
            if (self.amem>=vc.mem) & (self.acpu >= vc.ncpu):
                for vm in self.vl:
                    if vm.name==vc.name:
                        if vm.state=='deleted':
                            return vc
                        else:
                            unable=1
                            print('VC Name already exist')
                if unable==0:
                    return vc
#         else:
#             print('Server in ', self.state, ' state. Unable to proceed')
            

    # provision the vm on this server. vc is the vconf of the vm, 
    # and vm is the myvm object passed by the mycrm object.
    # if the acpu and mem is not sufficient return None.
    # increment the self.nvms 
    # no state transitions happen here, as provisioning process has not
    # been completed it with commit. If an undo happens, whatever you do
    # here will be undone by the mycrm.provision_undo() by calling 
    # myobj.deprovision_vm()

    
    def provision_vm(self, vc, vm):
        if self.can_provision(vc)==vc:
            self.vl.add(vm)
            self.amem-=vc.mem
            self.acpu-=vc.ncpu
            self.nvms+=1
            vm.state='provision'
            return vm
            
            
            
            
    # deprovision the vm on t his server. Recover the mem and cpu given.
    # decrement the self.nvms
    # called by mycrm.deprovision_vm()
    # do the staate transitions.

    def deprovision_vm(self, vm):
        new_list=mylist('list')
#         for v_machine in self.vl:
#             if v_machine!=vm:
#                 new_list.add(v_machine)
# #                 v_machine.state='deleted'
#         self.vl=new_list
        self.amem+=vm.amem
        vm.state='deleted'
        self.acpu+=vm.acpu
        self.nvms-=1
        self.stats['vprovision']-=1
        self.stats['vtotal']-=1
        self.stats['vdeleted']+=1


    # commit the provisioning of the vm. at this point do the state
    # transitions and book keeping accordingly and mark the vm as 
    # active, using the vm.set_active() function.
    # raise exception if the vm is not already bound to you. (you will maintain
    # that. 

    def commit_vm(self, vm):
        for vm_iter in self.vl:
            if vm_iter==vm:
                if vm_iter.state=='deleted':
                    pass
                else:
                    vm_iter.set_active(self)
                    if self.state=='idle':
                        self.state='active'
                        self.stats['sactive']+=1
                        self.stats['sidle']-=1
                    self.stats=vm_iter.stats

    # delete the server. raise exceptions if there are vms bound to it, and
    # active or provision vms. 
    # check the state transition requirements and do the state changes and book
    # keeping for the stats.
    # called by the mycrm.delete_server() routine.

    def delete(self):
        #YOUR CODE
        raise NotImplementedError

    # Fail the server. Move all the bound vms to idle, by calling
    # myvm.set_idle() routine, and recover all the memory and cpu given, and
    # reduce the self.nvms value approopriately. Move the state to 'fail'. and
    # do the right book keeping depending on the initial state which could be
    # 'idle' or 'active'.
    # note that no one will fail a server when there are vms in 'provision'
    # state. A previous provision_vm() operation either has to undo or commit
    # and the vm will go to 'active'(commit) or be deleted (undo)

    def fail(self):
        #YOUR CODE
        raise NotImplementedError

    # unfail the server. change the state from 'fail' to 'idle'. Raise exception
    # if the initial state is not 'fail'.

    def unfail(self):
        #YOUR CODE
        raise NotImplementedError
    
    # This has to be kept as is!! used by test cases and mycrm object.
    # to get the list of vm's bound to this server based on state. state could
    # be 'idle', 'active', and 'provision'.
    # returns the python list, and this should be the only place where python
    # list is used in this file.
    # if state is 'any' returns all.

    def get_vms(self, state):
        return_list=[]
        for vm in self.vl:
            if state=='any':
                if vm.state!='deleted':
                    return_list.append(vm)
            elif state==vm.state:
                if vm.state!='deleted':
                    return_list.append(vm)
        return return_list

