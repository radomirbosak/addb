# -*- coding: utf-8 -*-

import subprocess

from .cache import load_cache


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


def _show_table(table, headers=None):
    """
    Print a 2d matrix of strings as a nice table (with header bars)

    Args:
        table: 2d matrix (list of lists of strings) of input data
        headers: Header row
    """
    col_lens = [max(len(cell) for cell in col) for col in zip(*table)]

    if headers:
        col_lens = [max(collen, len(title)) for collen, title in zip(col_lens, headers)]
        for collen, title in zip(col_lens, headers):
            print(title.ljust(collen), end='  ')
        print('')

    # header line
    for collen in col_lens:
        print('=' * collen, end='  ')
    print('')

    # table data
    for row in table:
        for cell, maxlen in zip(row, col_lens):
            print(cell.ljust(maxlen), end='  ')
        print('')


def _get_terminal_size():
    rows, columns = subprocess.check_output(['stty', 'size']).split()
    return rows, columns
