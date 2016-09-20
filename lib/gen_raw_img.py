#!/usr/bin/env python

# ---------------------------------------
# This script uses to generate raw image
# of format .1 for converting to pnm.
# Written by Xiaoming Zhao
# ---------------------------------------

import os
import sys
import subprocess

BIN_PAR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.path.pardir))
BIN = os.path.join(BIN_PAR, 'ljpeg', 'jpegdir', 'jpeg')

print BIN_PAR
print BIN

if not os.path.exists(BIN):
    print 'ljpeg\'s jpeg has not been built yet!'\
          'Use cd ljpeg/jpegdir & make first!\n'
    sys.exit(0)


def gen_raw_img(path):
    cmd = '%s -d -s %s' % (BIN, path)
    subprocess.check_output(cmd, shell=True)
    path_prefix = os.path.dirname(path)
    filename = os.path.basename(path)
    new_filename = filename + '.1'
    new_path = os.path.join(path_prefix, new_filename)

    return new_path
