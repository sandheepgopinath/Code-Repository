# Add a server
[+] Check if a server with the same name exist
[+] If not , do the following book keeping
    -> stats['stotal']+=1
    -> stats['sidle']+=1
    
    
# Delete VM

[+] Check if a VM with same name exist. If not raise exception
[+] Else, Check the status
[+] If VM is in Active State, 
    -> 