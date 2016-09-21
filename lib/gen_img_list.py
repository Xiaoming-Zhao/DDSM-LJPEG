#!/usr/bin/env python

# ----------------------------------------------
# This script is for generating image index list
# from imdb_IRMA.
# Written by Xiaoming Zhao
# ----------------------------------------------

import sys
import os
import argparse

ROOT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.path.pardir()))


def gen_img_list(path):

    img_index_list = {}
    img_num = 0

    for (dirpath_s, dirname_s, filename_s) in os.walk(path):
        for filename in filename_s:
            img_num = img_num + 1

            filename_split = filename.split('.')
            LJPEG_index = filename_split.index('LJPEG')
            img_index = '.'.join(filename_split[:LJPEG_index])
            img_index_list[img_index] = filename

    print 'The total image number is {}.\n\n'.format(img_num)

    return img_index_list


def parse_args():
    parser = argparse.ArgumentParser(
        description='Generate the image list file of imdb_IRMA')
    parser.add_argument('--imdb', dest='imdb_path',
                        help='Set the path of imdb_IRMA.')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()

    imdb_path = args.imdb_path

    img_index_list = gen_img_list(imdb_path)

    img_list_file = os.path.join(ROOT_PATH, 'img_index_list.txt')
    print 'Generating image index list of imdb_IRMA ...\n'

    # Write the list to file
    with open(img_list_file, 'w') as f:
        for item in img_index_list.keys():
            f.write('{} {}\n'.format(item, img_index_list[item]))

    print '... done\n'
    print 'The file of imdb_IRMA\'s image index list is at {}.\n\n'\
          .format(img_list_file)
