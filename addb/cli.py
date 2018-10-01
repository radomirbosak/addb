# -*- coding: utf-8 -*-

import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-V', '--version', action='store_true',
                        help='show program version')
    parser.add_argument('-C', '--cache', help='specify cache file. '
                        'Default is addb.json in the $XDG_CACHE_HOME directory.')

    subparsers = parser.add_subparsers(dest='action')

    # export command
    subp_exp = subparsers.add_parser('export', help='Export anime/drama database')

    # list command
    subp_list = subparsers.add_parser('list', help='List anime/dramas in database')

    # add command
    subp_add = subparsers.add_parser('add', help='Add anime/drama to database')
    subp_add.add_argument('name', help='Short anime/drama name for use in CLI')
    subp_add.add_argument('--full-name', help='Full anime/drama name')
    subp_add.add_argument('--alias', action='append', default=[],
                          help='Alternative name for anime/drama. Can be specified '
                               'multiple times.')
    subp_add.add_argument('--status', default='unwatched',
                          choices=['unwatched', 'watching', 'watched', 'dropped'],
                          help='Anime/drama status')
    subp_add.add_argument('--watch-url', help='Url with the anime/drama stream')

    return parser.parse_args()
