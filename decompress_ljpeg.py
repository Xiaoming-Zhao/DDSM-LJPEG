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
DDSM_SOFTWARE_PATH = './ddsm/ddsm-software/ddsmraw2pnm'


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
        img_index = split_line[0].upper()
        nrow = split_line[2]
        ncol = split_line[4]
        ics_info[img_index] = {'nrow': nrow, 'ncol': ncol}

    return ics_info


def parse_args():
    parser = argparse.ArgumentParser(description='Read DDSM\'s ics file')
    parser.add_argument('--dir', dest='dir_path',
                        help='Set the DDSM images\'s directory.')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()

    dir_path = args.dir_path
    ics_path = glob.glob(os.path.join(dir_path, '*.ics'))
    img_path = glob.glob(os.path.join(dir_path, '*.LJPEG'))

    # get information from .ics file
    assert ics_path != [],\
        'There does not exist .ics file: {}.\n'.format(dir_path)
    assert len(ics_path) == 1,\
        'There exist two .ics files: {}.\n'.format(dir_path)

    ics_info = get_info_from_ics(ics_path[0])

    # decompress .LJPEG to raw image of type .1
    ljpeg_dict = {}

    assert img_path != [],\
        'There does not exist .LJPEG files: {}.\n'.format(dir_path)

    for ljpeg_path in img_path:

        gen_raw_img(ljpeg_path)

        # get angle index of file
        file_name = os.path.basename(ljpeg_path)
        ljpeg_dict[file_name] = {}
        view_index = file_name.split('.')[1].upper()
        ljpeg_dict[file_name]['view'] = view_index

        # get raw image path
        dir_name = os.path.dirname(ljpeg_path)
        raw_img_path = os.path.join(dir_name, file_name + '.1')
        ljpeg_dict[file_name]['raw_image'] = raw_img_path

        # get corresponding row and column number from ics file
        # print the command for transforming to .pnm file
        variable_list = [DDSM_SOFTWARE_PATH, raw_img_path,
                         ics_info[view_index]['nrow'],
                         ics_info[view_index]['ncol'],
                         ics_info['digitizer_type']]
        print '{} {} {} {} {}'.format(*variable_list)
