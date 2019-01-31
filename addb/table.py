# -*- coding: utf-8 -*-

import subprocess


def show_table(table, headers=None):
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


def get_terminal_size():
    rows, columns = subprocess.check_output(['stty', 'size']).split()
    return rows, columns
