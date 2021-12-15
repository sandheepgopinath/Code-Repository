sc=sconf(name,ncpu,mem)
        self.sc=sc
        server=None
        duplicate_exist_flag=0
        for server in self.server_list:
            if server.sc.name==sc.name:
                if server.state=='deleted':
                    server.state='idle'
                    server=server
                    server.amem=sc.mem
                    server.acpu=sc.ncpu
                    server.sconf=sc
                    server.nvms=0
                    self.stats['sidle']+=1
                    self.stats['stotal']+=1
                    
                    if self.unprovisioned.size>0:
                        for i in range(self.unprovisioned.size):
                            server.vl.add(vm)
                            unprov_vm=self.unprovisioned.pop()
                            unprov_vm.sr=server
                            server.amem-=unprov_vm.amem
                            server.acpu-=unprov_vm.acpu
                            server.nvms+=1
                        self.commit_provisioned_vms()
                else:
                    server=myserver(sc,self.stats)
                    server=server
                    server.state='idle'
                    server.amem=sc.mem
                    server.acpu=sc.ncpu
                    server.sconf=sc
                    server.nvms=0
                    if self.unprovisioned.size>0:
                        for i in range(self.unprovisioned.size):
                            unprov_vm=self.unprovisioned.pop()
                            unprov_vm.sr=server
                            self.provision_list.push(unprov_vm)
                            server.vl.add(unprov_vm)
                            server.amem-=unprov_vm.amem
                            server.acpu-=unprov_vm.acpu
                            server.nvms+=1
                    self.commit_provisioned_vms()
                    self.server_list.add(self.server)

        return server