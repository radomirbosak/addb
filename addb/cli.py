# -*- coding: utf-8 -*-

import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-V', '--version', action='store_true',
                        help='show program version')

    return parser.parse_args()
