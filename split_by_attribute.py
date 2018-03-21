import os
import shutil
import numpy as np
import cv2
import tensorflow as tf
import argparse


def mkdir_if_missing(path):
    if not os.path.exists(path):
        os.makedirs(path)


def main():
    parser = argparse.ArgumentParser(description='test', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-a', '--attribute',
                        default='Eyeglasses',
                        type=str,
                        help='Specify attribute name for training')
    parser.add_argument('-d', '--data_dir',
                        default='C:/workshop/face-attribute/datasets/celebA',
                        type=str,
                        help='Path of Data:align by 5 p')
    parser.add_argument('-ad1', '--attribute_dir1',
                        default='C:/workshop/face-attribute/datasets/celebA/Eyeglass',
                        type=str,
                        help='Path of images with eyeglass')
    parser.add_argument('-ad2', '--attribute_dir2',
                        default='C:/workshop/face-attribute/datasets/celebA/None-Eyeglass',
                        type=str,
                        help='Path of images without eyeglass')
    args = parser.parse_args()

    mkdir_if_missing(args.attribute_dir1)
    mkdir_if_missing(args.attribute_dir2)

    with open(os.path.join(args.data_dir, 'list_attr_celeba.txt'), 'r') as f:
        lines = f.read().strip().split('\n')
        col_id = lines[1].split().index(args.attribute) + 1
        attribute = list(map(int, [x.split()[col_id] for x in lines[2:]]))

    idxs1 = list(filter(lambda x: attribute[x] == 1, range(len(attribute))))
    idxs2 = list(filter(lambda x: attribute[x] == -1, range(len(attribute))))
    filenames1 = [os.path.join(args.data_dir, 'align_5p/{:06d}.jpg'.format(idx + 1)) for idx in idxs1]
    filenames2 = [os.path.join(args.data_dir, 'align_5p/{:06d}.jpg'.format(idx + 1)) for idx in idxs2]

    for srcfile in filenames1:
        if not os.path.isfile(srcfile):
            print("{} not exist!" .format(srcfile))
        else:
            fpath, fname = os.path.split(srcfile)
            dstfile = os.path.join(args.attribute_dir1, fname)
            shutil.copyfile(srcfile, dstfile)

    for srcfile in filenames2:
        if not os.path.isfile(srcfile):
            print("{} not exist!" .format(srcfile))
        else:
            fpath, fname = os.path.split(srcfile)
            dstfile = os.path.join(args.attribute_dir2, fname)
            shutil.copyfile(srcfile, dstfile)


if __name__ == "__main__":
    main()
