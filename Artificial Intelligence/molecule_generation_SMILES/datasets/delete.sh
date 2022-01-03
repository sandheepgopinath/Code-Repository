#! bin/bash

# Saving the list of all files into a files
ls | grep $1 > files

for file in $(cat files); do
	rm $file

done

rm files
