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
    subp_list.add_argument('--raw-alias-list', action='store_true',
                           help='Print only anime names and aliases, one per each '
                                'line. Useful for shell completion.')
    subp_list.add_argument('--raw-alias-list-desc', action='store_true',
                           help='List anime names and aliases for fish shell '
                                'completion.')

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

    # watch command
    subp_watch = subparsers.add_parser('watch', help='Open the anime/drama watch-url '
                                                     'in a web browser')
    subp_watch.add_argument('name', help='Anime name or alias')

    # remove command
    subp_remove = subparsers.add_parser('remove', help='Remove anime/drama from DB')
    subp_remove.add_argument('name', help='Anime name or alias')

    # update command
    subp_update = subparsers.add_parser('update',
                                        help='Set the number of watched episodes')
    subp_update.add_argument('name', help='Anime name or alias')
    subp_update.add_argument('episode', nargs='?',
                             help='Optional. The number of last watched episode. '
                                  'If not specified, the number of watched episodes '
                                  'is incremented by 1.')

    # edit command
    subp_edit = subparsers.add_parser('edit', help='Edit anime/drama properties')
    subp_edit.add_argument('name', help='Anime name or alias')
    subp_edit.add_argument('--full-name', help='Full anime/drama name')
    subp_edit.add_argument('--alias', action='append',
                          help='Alternative name for anime/drama. Can be specified '
                               'multiple times.')
    subp_edit.add_argument('--status',
                          choices=['unwatched', 'watching', 'watched', 'dropped'],
                          help='Anime/drama status')
    subp_edit.add_argument('--watch-url', help='Url with the anime/drama stream')

    return parser.parse_args()
