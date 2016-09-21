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
    os.path.join(os.path.dirname(__file__), os.path.pardir))


def gen_img_list(path):

    img_index_list = {}
    img_num = 0

    for (dirpath_s, dirname_s, filename_s) in os.walk(path):
        for filename in filename_s:
            img_num = img_num + 1

            filename_split = filename.split('.')
            # print '{}\n'.format(filename_split)
            # LJPEG_index = filename_split.index('LJPEG')
            img_index = '.'.join(filename_split[:2])

            # add img_index to dict
            # we need to check whether there already exist the key
            if img_index in img_index_list.keys():
                img_index_list[img_index].append(filename)
            else:
                img_index_list[img_index] = []
                img_index_list[img_index].append(filename)

    result_dict = {'list': img_index_list, 'img_num': img_num}

    return result_dict


def parse_args():
    parser = argparse.ArgumentParser(
        description='Generate the image list file of imdb_IRMA')
    parser.add_argument('--imdb', dest='imdb_path',
                        help='Set the path of imdb_IRMA.')
    parser.add_argument('--file', dest='img_list_file',
                        help='Set the writing path for image index list file.')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()

    imdb_path = args.imdb_path

    # generate the image list
    print 'Generating image index list of imdb_IRMA ...'
    result_dict = gen_img_list(imdb_path)
    print '... done\n\n'
    print 'The total image number is {}.\n\n'.format(result_dict['img_num'])

    # Write the list to file
    img_index_list = result_dict['list']

    img_list_file = args.img_list_file
    print 'Writing image list to file ...'

    with open(img_list_file, 'w') as f:
        for item in img_index_list.keys():
            info_list = [item]
            info_list.extend(img_index_list[item])
            if len(info_list) == 2:
                f.write('{} {}\n'.format(*info_list))
            else:
                f.write('{} {} {}\n'.format(*info_list))

    print '... done\n'
    print 'The file of imdb_IRMA\'s image index list is at {}.\n\n'\
          .format(img_list_file)
