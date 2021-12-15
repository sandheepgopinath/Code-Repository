# Create a sample file from kernel-0.files

f=open('kernel-0.files','r')
fw=open('kernel-1.files','w')

for i in range(30):
    fw.write(f.readline())

f.close()
fw.close()
print('File created')
