#! bash/sh:qw
python ./test1.py ./kernel-0.files > cmpout
if [[ $? != 0 ]]
then
	echo "test.py failed "
	exit 1
fi

sort cmpout > cmpout.sort
diff cmpout.sort output.sort > output_diff 2>&1
if  [[ $? != 0 ]]
then
	echo "tree traverse output failed see output_diff"
	exit 1
fi

echo "Correct output produced. Test pased". # still verify manually !!
