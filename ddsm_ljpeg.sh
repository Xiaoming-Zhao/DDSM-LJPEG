#!/usr/bin/env bash

# get the script directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $DIR

ljpeg2raw=$DIR/lib/decompress_ljpeg.py
raw2pnm=$DIR/ddsm/ddsm-software/ddsmraw2pnm
change_name=$DIR/lib/change_name.py
path=/home/xmchiu/Mammo_Challenge/DDSM/test_images/test_case

echo "path is $path"
echo $raw2pnm

cd $path

for sub_path in $(ls)
do
	cd $sub_path
	cur_path=$(pwd)
	echo "Current path is $cur_path"

	# run python script
	# to convert .LJPEG to raw image
	raw2pnm_command_split=$(python $ljpeg2raw --dir $cur_path --raw2pnm $raw2pnm)
	# echo $raw2pnm_command

	# convert raw image to .pnm format
	i=0
	for item in $raw2pnm_command_split
	do
		let "i=$i+1"

		# check whether the new command begins
		let "v=$i%5"
		first_flag=$[$v==1]
		# echo $i
		# echo $item

		# check whether a full command ends
		let "u=$i%5"
		round_flag=$[$u==0]
		if [ $first_flag == '1' ];then
			raw2pnm_command=$item
		else
			raw2pnm_command=$raw2pnm_command" "$item
		fi

		if [ $round_flag == '1' ];then
			echo $raw2pnm_command
			$raw2pnm_command
		fi

	done

	cd ..
done

