#!/usr/bin/env bash

path=/home/xmchiu/Mammo_Challenge/DDSM/test_images/test_case
echo "path is $path"

cd $path

for sub_path in $(ls)
do
	cd $sub_path
	cur_path=$(pwd)
	echo "Current path is $cur_path"
done
