#!/usr/bin/env python

# --------------------------------------
# This script is for getting information
# from DDSM .ics files.
# Written by Xiaoming Zhao
# --------------------------------------

import os
import sys
import numpy as np
import linecache
import argparse
import glob
from gen_raw_img import gen_raw_img


DIGITIZER_CLASSES = ['dba', 'howtek-mgh', 'howtek-ismd', 'lumisys']


def get_info_from_ics(path):

    ics_info = {}

    with open(path, 'r') as ics_file:
        pre_ics_content = [item.strip() for item in ics_file.readlines()]
    ics_content = pre_ics_content[-6:]

    # Get the digitizer type from .ics file
    pre_inst_code = pre_ics_content[2].split(' ')[1]
    inst_code = pre_inst_code.split('-')[0].upper()
    pre_digitizer_type = ics_content[0].split(' ')[1].lower()

    if pre_digitizer_type == 'howtek':
        if inst_code == 'A':
            digitizer_type = 'howtek-mgh'
        if inst_code == 'D':
            digitizer_type = 'howtek-ismd'
    else:
        digitizer_type = pre_digitizer_type

    assert digitizer_type in DIGITIZER_CLASSES,\
        'Wrong digitizer type: {}!\n'.format(digitizer_type)

    ics_info['digitizer_type'] = digitizer_type

    # Find each image's number of rows and columns
    img_info = ics_content[-4:]
    for img_line in img_info:
        split_line = img_line.split(' ')
        img_index = split_line[0]
        nrow = split_line[2]
        ncol = split_line[4]
        ics_info[img_index] = {'nrow': nrow, 'ncol': ncol}

    return ics_info


def args_parse():
    parser = argparse.ArgumentParser(description='Read DDSM\'s ics file')
    parser.add_argument('--dir', des='dir_path',
                        help='Set the DDSM images\'s directory.')

    print len(sys.argv)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = args_parse()

    dir_path = args.dir_path
    ics_path = glob.glob(os.path.join(dir_path, '*.ics'))
    img_path = glob.glob(os.path.join(dir_path, '*.LJPEG'))

    # get information from .ics file
    assert ics_path != [],\
        'There does not exist .ics file: {}.\n'.format(dir_path)

    ics_info = get_info_from_ics(ics_path)

    # decompress .LJPEG to raw image of type .1
    assert img_path != [],\
        'There does not exist .LJPEG files: {}.\n'.format(dir_path)

    for ljpeg_path in img_path:
        gen_raw_img(ljpeg_path)
