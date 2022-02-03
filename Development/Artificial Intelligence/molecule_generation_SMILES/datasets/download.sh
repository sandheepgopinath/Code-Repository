#! bin/bash


if (($1 == gdb13))
then
	wget https://zenodo.org/record/5172018/files/gdb13.tgz?download=1
elif (($1 == gdb17))
then
	wget https://zenodo.org/record/5172018/files/GDB17.50000000.smi.gz?download=1
elif (($1 == gdb11))
then 
	wget https://zenodo.org/record/5172018/files/gdb11.tgz?download=1
else
	echo [+] Invalid Argument
fi


