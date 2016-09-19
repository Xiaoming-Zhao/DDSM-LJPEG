#!/usr/bin/env python

# --------------------------------------
# This script is for getting information
# from DDSM .ics files.
# Written by Xiaoming Zhao
# --------------------------------------

import os
import numpy as np
import linecache
import argparse
import glob
from gen_raw_img import gen_raw_img


DIGITIZER_CLASSES = ['dba', 'howtek-mgh', 'howtek-ismd', 'lumisys']


def args_parse():
    parser = argparse.ArgumentParser(description='Read DDSM\'s ics file')
    parser.add_argument('--dir', des='dir',
                        help='Set the DDSM images\'s directory.')

    args = parser.parse_args()

    return args


def get_info_from_ics(path, im_index):

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




if __name__ = '__main__':
    args = parse_args()

    dir_path = args.dir
    ics_path = glob.glob(os.path.join(dri_path, '*.ics'))
    img_path = glob.glob(os.path.join(dri_path, '*.LJPEG'))
