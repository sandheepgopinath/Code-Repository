import os
import sys
from mylist import *
from mycrm import *
from myserver import *
from myvm import *
from inspect import currentframe, getframeinfo

# test.py for toy cloud assignment.
# feel free to comment the relevant parts in main function.

## test helper functions

global test_no
global crm
test_no=0
def mycheck(result, msg, lno=0):
    global test_no
    test_no += 1
    cf=currentframe()
    l1=cf.f_back.f_lineno
    if lno:
        l=f'{lno},{l1}'
    else:
        l=f'{l1}'
    if result:
        print(f'{l} tno: {test_no} {msg} PASSED ')
    else:
        print(f'{l}: tno: {test_no} {msg} FAILED ')
        sys.exit(1)

# template crmstat to copy and change values.
#mys=crm_stat(stotal=1,sidle=1,sactive=0,sfail=0,vtotal=1,vprovision=1,vactive=0,'vidle', vdeleted=0)
#print(mys)


def check_stat(s1):
    cf=currentframe()
    lno=cf.f_back.f_lineno
    s=crm.get_stat()
    mycheck((s==s1),f'{s1} == {s}', lno)

def check_server_count(count, state):
    cf=currentframe()
    lno=cf.f_back.f_lineno

    s=crm.get_servers(state)
    mycheck(len(s) == count, f'server_count {len(s)} == {count} for state {state}', lno)

    s=crm.get_servers('any')
    c=0
    for i in s:
        if state != 'any' and i.state != state:
            continue
        c += 1
    mycheck(c == count, f'server_count {c} == {count} for state {state}', lno)

def check_server_state(sname, state):
    cf=currentframe()
    lno=cf.f_back.f_lineno
    assert(state != 'any')
    s=crm.get_servers('any')
    f=0
    for i in s:
        if i.sc.name == sname and i.state == state:
            f=1
            break
    mycheck(f==1, f'server {sname} with state {state} found', lno)
    s=crm.get_servers(state)
    f=0
    for i in s:
        if i.sc.name == sname and i.state == state:
            f=1
            break
    mycheck(f==1, f'server {sname} with state {state} found', lno)

def check_vm_count(count, state):
    cf=currentframe()
    lno=cf.f_back.f_lineno
    s=crm.get_vms(state)
    mycheck(len(s) == count, f'vm count {len(s)} == {count} for state {state}', lno)

    s=crm.get_vms('any')
    c=0
    for i in s:
        if state != 'any' and i.state != state:
            continue
        c += 1
    mycheck(c == count, f'vm count {c} == {count} for state {state}', lno)
    c=0
    s=crm.get_servers('any')
    for i in s:
        v=i.get_vms(state)
        for j in v:
            c += 1
    mycheck(c == count, f'vm count {c} == {count} for state {state}', lno)
    c=0
    s=crm.get_servers('any')
    for i in s:
        v=i.get_vms('any')
        for j in v:
            if state != 'any' and j.state != state:
                continue
            c += 1
    mycheck(c == count, f'vm count {c} == {count} for state {state}', lno)



def check_server_vm_count(sr, count, state):
    cf=currentframe()
    lno=cf.f_back.f_lineno

    s=crm.get_servers('any')
    f=0
    for i in s:
        if i.sc.name == sr:
            f=1
            fs=i
            break
    if f != 1:
        mycheck(0, f'server {sr} lookup', lno)

    v=fs.get_vms('any')
    c=0
    for i in v:
        if state != 'any' and i.state != state:
            continue
        c += 1
    mycheck(c==count, f'vm count in {sr} {c} == {count} for state={state}', lno) 
    if state == 'any':
        return
    v=fs.get_vms(state)
    c=0
    for i in v:
        c += 1
    mycheck(c==count, f'vm count in {sr} {c} == {count} for state={state}', lno) 

def check_server_vm_state(sr, vm, state):
    cf=currentframe()
    lno=cf.f_back.f_lineno
    s=crm.get_servers('any')
    f=0
    for i in s:
        if i.sc.name == sr:
            f=1
            fs=i
            break
    if f != 1:
        mycheck(0, f'server {sr} lookup', lno)

    v=crm.get_vms('any')
    f=0
    for i in v:
        if i.vc.name == vm:
            f=1
            fv=i
            break
    if f != 1:
        mycheck(0, f'vm {vm} in {sr} lookup', lno)
    mycheck(fv.state==state, f'vm: {fv.vc.name} state {fv.state} == {state}', lno) 

def check_novm(vm):
    cf=currentframe()
    lno=cf.f_back.f_lineno

    s=crm.get_vms('any')
    c=0
    for i in s:
        if i.vc.name == vm:
            c += 1
    mycheck(c == 0, f'vm {vm} not present', lno)
    c=0
    s=crm.get_servers('any')
    for i in s:
        v=i.get_vms('any')
        for j in v:
            if j.vc.name == vm:
                c += 1
    mycheck(c == 0, f'vm {vm} not present', lno)

def check_server_novm(sr, vm):
    cf=currentframe()
    lno=cf.f_back.f_lineno
    s=crm.get_servers('any')
    f=0
    for i in s:
        if i.sc.name == sr:
            f=1
            fs=i
            break
    if f != 1:
        mycheck(0, f'server {sr} lookup', lno)

    v=crm.get_vms('any')
    f=0
    for i in v:
        if i.vc.name == vm:
            f=1
            fv=i
            break
    mycheck(f==0, f'vm: {vm}  in server {sr} not present', lno) 
## tests start

def crm_server():
    global crm
    crm=mycrm()
    a = crm.add("s1", 500, 1000)
    print(a.sc)
    check_server_count(1, 'any')
    s=crm.get_servers('any')
    mycheck((len(s) == 1), "get servers should return one entry")
    check_server_count(1, 'idle')
    check_server_state('s1', 'idle')
    s=crm.get_stat()
    check_stat(crm_stat(stotal=1,sidle=1))
    crm.fail(a.sc.name)
    check_stat(crm_stat(stotal=1,sfail=1))
    check_server_state('s1', 'fail')
    crm.unfail(a.sc.name)
    check_stat(crm_stat(stotal=1,sidle=1))
    check_server_state('s1', 'idle')
    crm.delete_server(a.sc.name)
    check_stat(crm_stat(sdeleted=1))
    check_server_count(0, 'any')
    
    print(f'*********crm_1server tests done *********')
    print(f'*********crm_1server tests done *********')

def crm_vm():
    global crm
    crm=mycrm()
    a = crm.add("s1", 500, 1000)
    print(a)
    check_server_state("s1", 'idle')
    v=crm.provision_vm("vm1", 2, 50)
    print(v)
    check_server_state("s1", 'idle')
    check_stat(crm_stat(stotal=1,sidle=1,vtotal=1,vprovision=1))
    check_vm_count(1, 'provision')
    check_vm_count(1, 'any')
    check_server_vm_state("s1", "vm1", 'provision')
    check_server_vm_count("s1", 1, 'provision')
    crm.commit_provisioned_vms()
    check_server_state("s1", 'active')
    check_server_vm_count("s1", 1, 'active')
    check_server_vm_state("s1", "vm1", 'active')
    check_stat(crm_stat(stotal=1,sactive=1,vtotal=1,vactive=1))
    check_vm_count(1, 'any')
    check_vm_count(1, 'active')
    te=0
    try:
        crm.delete_server("s1")
    except Exception as e:
        te=1
    mycheck(te == 1, 'Cannot delete an active server')

# provision one more vm and then undo it.
    v=crm.provision_vm("vm2", 2, 50)
    print(v)
    check_stat(crm_stat(stotal=1,sactive=1,vtotal=2,vprovision=1,vactive=1))
    check_vm_count(2, 'any')
    check_vm_count(1, 'active')
    check_vm_count(1, 'provision')
    check_server_vm_count("s1", 1, 'active')
    check_server_vm_state("s1", "vm1", 'active')
    check_server_vm_count("s1", 1, 'provision')
    check_server_vm_state("s1", "vm2", 'provision')
    crm.provision_undo(1)
    check_stat(crm_stat(stotal=1,sactive=1,vtotal=1,vactive=1,vdeleted=1))
    check_vm_count(1, 'any')
    check_server_vm_count("s1", 1, 'any')
    check_server_vm_count("s1", 1, 'active')
    check_novm("vm2")
    check_server_novm("s1", "vm2")
    te=0
    try:
        crm.delete_vm('random')
    except Exception as e:
        te=1
    mycheck(te == 1, 'Wrong name to delete')
    crm.delete_vm("vm1")
    check_vm_count(0, 'any')
    check_server_vm_count("s1", 0, 'any')
    check_novm("vm1")
    check_server_novm("s1", "vm1")
    check_stat(crm_stat(stotal=1,sidle=1,vdeleted=2))
    crm.delete_server(a.sc.name)
    check_stat(crm_stat(vdeleted=2,sdeleted=1))
    check_server_count(0, 'any')
    check_vm_count(0, 'any')
    print(f'********crm_1vm tests done ************')
    print(f'********crm_1vm tests done ************')

aggr=namedtuple('aggr', 'ncpu mem')
vmt=namedtuple('vmt', 'ncpu mem')
testvm=namedtuple('testvm', 'vc pvm')

def get_available():
    available_cpus=0
    available_mem=0
    avails=[]
    s=crm.get_servers('any')
    for i in s:
        available_cpus += i.acpu
        available_mem += i.amem
        avails.append(sconf(i.sc.name, i.acpu, i.amem))

    print(avails)
    y=aggr(available_cpus, available_mem)
    return y
         

def crm_nvms():
    global crm
    crm=mycrm()
    # 10 servers, 1000 vms
    ps=[]
    nservers=10
    for i in range(0,nservers):
        sname=f's{i}'
        a = crm.add(sname, 150+i*50, 1000+2*i*200)
        ps.append(a)
    print (f'Physical Servers: {ps}')
    total_memory=0
    total_cpu=0
    for i in ps:
        total_memory +=i.sc.mem
        total_cpu += i.sc.ncpu
    total = aggr(total_cpu,total_memory)
    print (total)
    t1=vmt(2, 4)
    t2=vmt(4,16)
    t3=vmt(8,64)
    t4=vmt(16,128)
    t5=vmt(32,256)
    t6=vmt(64,512)
    t7=vmt(128,1024)
    vmtypes=[t1, t2, t3, t4, t5, t6, t7]
    print(vmtypes)
    # keep allocating until we run out of space
    i=0
    v=0
    vms=[]
    pvms=[]
    mod=len(vmtypes) 
    while True:
        vname=f'vm{v}'
        ncpu=vmtypes[i].ncpu
        mem=vmtypes[i].mem
        vm = crm.provision_vm(vname, ncpu, mem)
        if vm == None:
            print(f'provisioning failed for {vmtypes[i]}')
            mod -= 1
            if mod == 0:
                break
        else:
            tvm=testvm(vm.vc,vm)
            vms.append(tvm)
            pvms.append(vm)
            v += 1
        i=(i+1)%mod


    allocated_cpus=0
    allocated_mem=0
#    print(vms)
    for v in pvms:
        allocated_cpus += v.vc.ncpu 
        allocated_mem += v.vc.mem 

    allocated=aggr(allocated_cpus, allocated_mem)
    available=get_available()
    print(f'allocated:{allocated} Total: {total} available:{available}')
    check_stat(crm_stat(stotal=nservers,sidle=nservers,sactive=0,sfail=0,vtotal=len(vms),vprovision=len(vms),vactive=0, vdeleted=0))

    vmtypes=[t1, t2, t3, t4, t5, t6, t7]
    for s in ps:
        check_server_state(s.sc.name, 'idle')
        check_vm_count(len(vms), 'provision')
        check_vm_count(len(vms), 'any')
        for v in s.get_vms('any'):
            check_server_vm_state(s.sc.name, v.vc.name, 'provision')
        check_server_vm_count(s.sc.name, s.nvms, 'provision')
        mycheck(((s.acpu < vmtypes[0].ncpu) or (s.amem < vmtypes[0].mem)),
                f'Server {s.sc.name, s.acpu, s.amem} available < min vm {vmtypes[0].ncpu}')

#undo last 10 operations

    crm.provision_undo(10)
    check_stat(crm_stat(stotal=nservers,sidle=nservers,sactive=0,sfail=0,vtotal=len(vms)-10,vprovision=len(vms)-10,vactive=0, vdeleted=10))

# verify that the last 10 vms are not present

    for i in range(0,10):
        v=vms[-i-1]
        pv=pvms[-i-1]
        check_novm(v.vc.name)
        mycheck((pv.state=='deleted'), f'vm {pv.vc.name} state {pv.state} == deleted')
#provision these vms again in the same order as before
    for i in range(0,10):
        v=vms[len(vms)-10+i]
        print(f'recreating {v.vc.name}')
        vm = crm.provision_vm(v.vc.name, v.vc.ncpu, v.vc.mem)
        tvm=testvm(vm.vc,vm)
        vms[len(pvms)-10+i]=tvm
        pvms[len(pvms)-10+i]=vm
    check_stat(crm_stat(stotal=nservers,sidle=nservers,sactive=0,sfail=0,vtotal=len(vms),vprovision=len(vms),vactive=0,
        vdeleted=10))


#now consume all cpus
    v=len(vms)
    print(v)
    while True:
        vname=f'vm{v}'
        ncpu=1
        mem=1
        vm = crm.provision_vm(vname, ncpu, mem)
        if vm == None:
            print(f'provisioning failed for {vname, ncpu, mem}')
            break
        tvm=testvm(vm.vc,vm)
        vms.append(tvm)
        pvms.append(vm)
        v += 1
    print(f'Provisioned total of {v} more vms')

    allocated_cpus=0
    allocated_mem=0
#    print(vms)
    for v in pvms:
        allocated_cpus += v.vc.ncpu 
        allocated_mem += v.vc.mem 

    allocated=aggr(allocated_cpus, allocated_mem)
    available=get_available()
    print(f'allocated:{allocated} Total: {total} available:{available}')
    check_stat(crm_stat(stotal=nservers,sidle=nservers,sactive=0,sfail=0,vtotal=len(vms),vprovision=len(vms),vactive=0, vdeleted=10))
        
   #commit all the vms

    crm.commit_provisioned_vms()
    check_stat(crm_stat(stotal=nservers,sidle=0,sactive=nservers,sfail=0,vtotal=len(vms),vprovision=0,vactive=len(vms), vdeleted=10))

# fail a server.
    for p in ps:
        print(f'server: {p.sc.name}')

    print(f'Failing few servers')
    nvms=ps[0].nvms+ps[1].nvms
    crm.fail(ps[0].sc.name)
    crm.fail(ps[1].sc.name)
    check_stat(crm_stat(stotal=nservers,sidle=0,sactive=nservers-2,sfail=2,vtotal=len(vms),vprovision=0,vactive=len(vms)-nvms,vidle=nvms, vdeleted=10))
    idlevms=crm.get_vms('idle')
    mycheck(len(idlevms)==nvms, f'idlevms count{len(idlevms)} match {nvms} vms in failed servers')




    print(f'Deleting few servers')
    crm.delete_server(ps[0].sc.name)
    print(f'Deleting few servers')
    crm.delete_server(ps[1].sc.name)
    check_stat(crm_stat(stotal=nservers-2,sidle=0,sactive=nservers-2,sfail=0,sdeleted=2,vtotal=len(vms),vprovision=0,vactive=len(vms)-nvms,vidle=nvms, vdeleted=10))

#now delete some 10 vms
    print(f'deleting 10 vms')
    for i in range(0,9):
        crm.delete_vm(f'vm{i}')
# delete one of this idle vms.
    
    idlevms=crm.get_vms('idle')
    v1=idlevms[0]
    print(f'deleting {v1.vc.name}')
    crm.delete_vm(v1.vc.name)
    nvms -= 1

# delete one idle vm

    check_stat(crm_stat(stotal=nservers-2,sidle=0,sactive=nservers-2,sfail=0,sdeleted=2,vtotal=len(vms)-10,vprovision=0,vactive=len(vms)-nvms-10,vidle=nvms, vdeleted=20))

#now reprovision the idle vms in those 10 vm slots.
    c=crm.provision_all_idle_vms()
    print(f'idle vms reprovisioned is {c}')
    check_stat(crm_stat(stotal=nservers-2,sidle=0,sactive=nservers-2,sfail=0,sdeleted=2,vtotal=len(vms)-10,vprovision=0,vactive=len(vms)-nvms-10+c,vidle=nvms-c, vdeleted=20))


# add the servers back
    vm=crm.get_vms('idle')
    for v in vm:
        print(f'idlevm: {v.vc}')
    print(f'Adding server config {ps[0].sc}')
    a=crm.add(ps[0].sc.name, ps[0].sc.ncpu, ps[0].sc.mem)
    ps[0]=a
    print(f'adding provisioned {a.nvms} vms')
    check_stat(crm_stat(stotal=nservers-1,sidle=1,sactive=nservers-2,sfail=0,sdeleted=2,vtotal=len(vms)-10,vprovision=0,vactive=len(vms)-nvms-10+c,vidle=nvms-c, vdeleted=20))
    
    print(f'Adding server config {ps[1].sc}')
    a=crm.add(ps[1].sc.name, ps[1].sc.ncpu, ps[1].sc.mem)
    ps[1]=a
    print(f'adding provisioned {a.nvms} vms')
    check_stat(crm_stat(stotal=nservers,sidle=1,sactive=nservers-1,sfail=0,sdeleted=2,vtotal=len(vms)-10,vprovision=0,vactive=len(vms)-nvms-10+c+1,vidle=nvms-c-1, vdeleted=20))

# fail and unfail the servers. all vms should be provisioned exactly as before.

    nvms1=ps[7].nvms
    print(f'Failing server {ps[7].sc} nvms1 idle: {nvms1}')
    crm.fail(ps[7].sc.name)
    check_stat(crm_stat(stotal=nservers,sidle=1,sactive=nservers-2,sfail=1,sdeleted=2,vtotal=len(vms)-10,vprovision=0,vactive=len(vms)-nvms-10+c+1-nvms1,vidle=nvms-c-1+nvms1, vdeleted=20))
    print(f'UnFailing server {ps[7].sc} nvms1 idle: {nvms1}')
    crm.unfail(ps[7].sc.name)
    pvms1=ps[7].nvms
    if pvms1 != nvms1:
        print(f'fail/unfail did not reprovision all idle vms')
        print(f'faill vms: {nvms} reprovision vms: {pvms1}')
    check_stat(crm_stat(stotal=nservers,sidle=1,sactive=nservers-1,sfail=0,sdeleted=2,vtotal=len(vms)-10,vprovision=0,vactive=len(vms)-nvms-10+c+1,vidle=nvms-c-1, vdeleted=20))

# now delete all physical servers

    for p in ps:
        print(f'server: {p.sc.name}')

    for p in ps:
        print(f'deleting {p.sc.name}')
        if p.nvms:
            te=0
            try:
                crm.delete_server(p.sc.name)
            except Exception as e:
                te=1
            s=f'active server {p.sc.name} should fail'
            mycheck(te==1, s)

# now delete all vms

#    for v in crm.get_vms('any'):
#        print(v.vc.name)
    for v in vms:
        try:
            crm.delete_vm(v.vc.name)
        except Exception as e:
            s=f'Delete_vm returned exception for {v.vc}'
            print(e)

# check for zero vms
    check_stat(crm_stat(stotal=nservers,sidle=nservers,sactive=0,sfail=0,sdeleted=2,vtotal=0,vprovision=0,vactive=0,vidle=0, vdeleted=130))

#delete all physical servers
    for p in ps:
        print(f'deleting {p.sc.name}')
        mycheck(p.nvms==0, f'Server {p.sc} should have zero vms. Found {p.nvms}')
        try:
            crm.delete_server(p.sc.name)
        except Exception as e:
            s=f'Idle server {p.sc.name} can be deleted'
            mycheck(0, s)

    check_stat(crm_stat(stotal=0,sidle=0,sactive=0,sfail=0,sdeleted=12,vtotal=0,vprovision=0,vactive=0,vidle=0, vdeleted=130))
        


def main():
    global crm
    crm=mycrm()
   
   # feel free to go through tests one by one. comment the other.
   # mycheck() will print the calling line no.s where it is called, and the
   # caller of that if it is called via a helper function  and the test no. 
    crm_server()
    crm_vm()
    #crm_nvms()

if __name__ == "__main__":
    main()
