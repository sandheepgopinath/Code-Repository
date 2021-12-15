Setting a VM to Active 
> Only VM in provision and idle state can be made active
> Failed VM's cannot be made active
> Different States of a VM : Idle,fail,active,provision,deprovision

> Function to be called during COMMIT or PROVISION IDLE

In Code : 
> If current state is Idle, change it to Active
> Book Keepings : stats['vidle']-=1, stats['vactive']+=1
> If Bound server is 'Idle' Change it to active

> If current state is Provision, change it to active
> Book Keepings : stats['vprovision']-=1, stats['vactive']+=1
> If Bound server is 'Idle' Change it to active

> Bind it to a server. self.sr=server



________________________________________________________________________



Setting a VM to Idle 
> Only VM's which are active can be moved into idle mode. 

> Function to be called during server FAIL to make all VM's idle
> Book keepings : stats['vactive']-=1, stats['idle']+=1
> Unbind server
> If all VM's on bound server are Idle, change status to Idle



