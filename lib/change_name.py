#!/usr/bin/env python

# -------------------------------------------------
# This script is for changing names of .png images.
# Written by Xiaoming Zhao
# -------------------------------------------------

import os
import sys
import glob
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Change png\'s name to match imdb_IRMA')
    parser.add_argument('--dir', dest='dir_path',
                        help='Set the .png images\'s directory.')
    parser.add_argument('--file', dest='img_list_file',
                        help='Set the imdb_IRMA image list\'s directory.')
    parser.add_argument('--repeat', dest='repeated_img_file',
                        help='Set the file directory for repeated iamges.')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()

    dir_path = args.dir_path

    # read the content of image list file
    img_list_file = args.img_list_file

    with open(img_list_file, 'r') as f:
        pre_img_list = [item.strip() for item in f.readlines()]

    # generate the image index list
    img_index_list = {}

    for line in pre_img_list:
        split_line = line.split(' ')
        img_index_list[split_line[0]] = []
        img_index_list[split_line[0]].extend(split_line[1:])

    # get the .png file list under the path
    png_list = []

    for (dirpath, dirname_s, filename_s) in os.walk(dir_path):
        for filename in filename_s:
            if filename.split('.')[-1].lower() == 'png':
                png_list.append(os.path.join(dirpath, filename))

    assert png_list != [],\
        'There does not exist .png file: {}.\n'.format(dir_path)

    print 'Find {} png images totally.\n'.format(len(png_list))

    # chagne png file name to match the name of imdb_IRMA
    print 'Changing name of png files ...'

    repeated_img_file = args.repeated_img_file
    rename_num = 0
    repeated_img_num = 0

    for png_file in png_list:
        png_dirname = os.path.dirname(png_file)
        png_filename = os.path.basename(png_file)
        file_index = '.'.join(png_filename.split('.')[:2])
        # print '{} {} {}\n'.format(png_dirname, png_filename, file_index)

        assert file_index in img_index_list.keys(),\
            'Wrong image index, imdb_IRMA does not include this image: {}.\n'\
            .format(png_file)

        new_filename_list = img_index_list[file_index]
        if len(new_filename_list) == 1:
            rename_num = rename_num + 1
            new_filename = new_filename_list[0]
            os.rename(png_file, os.path.join(png_dirname, new_filename))
        else:
            repeated_img_num = repeated_img_num + 1
            info_list = [file_index]
            info_list.extend(new_filename_list)
            info_list.append(png_file)
            with open(repeated_img_file, 'a') as f:
                f.write('{} {} {} {}\n').format(*info_list)

    print '... done'
    print 'Rename {} images.\nWrite {} repeated images to {}.\n'\
        .format(rename_num, repeated_img_num, repeated_img_file)
