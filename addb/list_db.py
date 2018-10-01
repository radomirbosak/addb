# -*- coding: utf-8 -*-

from .cache import load_cache


def list_db(args):
    """
    List entries in anime/drama database
    """
    cache = load_cache(args.cache)
    headers = ['nr.', 'Name', 'Status', 'Progress']

    table = []

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
