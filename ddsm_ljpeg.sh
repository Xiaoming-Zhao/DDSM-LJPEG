#!/usr/bin/env bash

ljpeg2raw=/home/xmchiu/Mammo_Challenge/DDSM/DDSM-LJPEG/decompress_ljpeg.py
path=/home/xmchiu/Mammo_Challenge/DDSM/test_images/test_case
echo "path is $path"

cd $path

for sub_path in $(ls)
do
	cd $sub_path
	cur_path=$(pwd)
	echo "Current path is $cur_path"

	# run python script
	# to convert .LJPEG to .1
	python ljpeg2raw $cur_path
	
	cd ..
done

