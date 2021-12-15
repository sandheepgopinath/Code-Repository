# Set Fail Function
[+] A Server in Idle or Active state can fail
[+] Once a server fails, do the following book keepings
    -> If server was active, self.stats['sactive']-=1, self.stats['sfail']+=1
    -> If server was idle, self.stats['sidle']-=1,self.stats['sfail']+=1
    -> Make all the VM's on the server Idle
    -> Set self.stats['sfail']+=1
    

# Set Active function

[+] Ideal to Active can happen during commiting
[+] Decrease sidle in stats, Increase sactive in stats
[+] This can be called during commit, when the VM's have to be activated, which inturn has to activate the server


# Can Provision function

[+] Server should be in idle or active state
[+] vconf with name, cpu and memory is input
[+] Check if the server has memory and cpu
[+] If same name exist, then cannot provision in same server
[+] Make no transitions as we are not commiting or provisioning


## Provision VM Function

[+] vconf object and VM object is the input
[+] Call the can_provision function, if success follow the next steps. 
[+] Reduce the VM's cpu and memory from server
[+] Increase the nvms by 1
[+] Add the server to provision_list ( Stack ) 
[+] vtotal,  vprovision should increase by 1
[+] Change state to provision


# Deprovision VM Function

[+] VM Object passed as input
[+] Find the Vm from Provision List
[+] Delete the element from list and VL
[+] Decrease nvms by 1
[+] Decrease vtotal,vprovision, by 1
[+] Increase deleted by 1
[+] Change state of Vm to deleted


## Commit a VM

[+] Check for the element in provision list
[+] Check for the element in vl list
[+] Once the element is found in both places, then 
    -> Set the status of VM to active
    -> stats['vprovision']-=1. stats['vactive']+=1
    -> 