# -*- coding: utf-8 -*-

import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-V', '--version', action='store_true',
                        help='show program version')
    parser.add_argument('-C', '--cache', help='specify cache file. '
                        'Default is addb.json in the $XDG_CACHE_HOME directory.')

    subparsers = parser.add_subparsers(dest='action')

    subp_exp = subparsers.add_parser('export', help='Export anime/drama database')

    return parser.parse_args()
