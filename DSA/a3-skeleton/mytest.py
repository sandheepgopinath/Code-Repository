from mycrm import *

mycrm=mycrm()

#Add a server
mycrm.add('Server1',10,100)
# Checking if the server has been created properly
print(mycrm.server)

print('\n Changing the state of the server to active for testing')

print(mycrm.server.state)

mycrm.delete_server('Server1')

print(mycrm.server)
