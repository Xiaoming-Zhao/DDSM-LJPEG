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
    parser = argparse.ArgumentParser(description='Read DDSM\'s ics file')
    parser.add_argument('--dir', dest='dir_path',
                        help='Set the .pnm images\'s directory.')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()

    dir_path = args.dir_path

    pnm_list = glob.glob(os.path.join(dir_path, '*.pnm'))
    assert pnm_list != [],\
        'There does not exist .pnm file: {}.\n'.format(dir_path)

    # chagne pnm file name to 
