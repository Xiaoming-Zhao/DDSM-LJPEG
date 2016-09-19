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
from gen_raw_img import gen_raw_img

def args_parse():
    parser = argparse.ArgumentParser(description='Read DDSM\'s ics file')
    parser.add_argument('--dir', des='file_dir',
                        help='Set the DDSM images\'s directory.')

    args = parser.parse_args()

    return args

