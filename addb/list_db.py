# -*- coding: utf-8 -*-

from .cache import load_cache
from .table import _show_table


def list_db(args):
    """
    List entries in anime/drama database
    """
    cache = load_cache(args.cache)
    headers = ['nr.', 'Name', 'Status', 'Progress']

    table = []

    # is the switch is present, print only names and aliases
    if hasattr(args, 'raw_alias_list') and args.raw_alias_list:
        for anime in cache['anime']:
            print(anime['name'])
            for alias in anime['alias']:
                print(alias)
        return

    if hasattr(args, 'raw_alias_list_desc') and args.raw_alias_list_desc:
        for anime in cache['anime']:

            description = '\t' + anime['full_name'] if anime['full_name'] else ''
            print(anime['name'] + description)
            for alias in anime['alias']:
                print(alias + description)
        return

    # print a nice table
    for idx, anime in enumerate(cache['anime'], 1):
        row = [
            str(idx) + '.',
            anime['full_name'] or 'N/A',
            anime['status'] or 'N/A',
            str(anime['progress'])
        ]
        table.append(row)

    _show_table(table, headers=headers)
