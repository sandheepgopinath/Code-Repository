import random as random

day=0
profit=0
loss=0

while(day<30):
    day+=1
    choice=str(random.randint(0,9))
    lottery=str(random.randint(0,9))
    status=choice==lottery
    temp=status+0
    
    lossStatus=not status
    lossTemp=lossStatus+0

    profit+=(temp*800)-(lossTemp*100)
print(profit)