# -*- config: utf-8 -*-

import os

from xdg.BaseDirectory import xdg_cache_home


def _determine_cache_filename(filename=None):
    """
    Determine cache filename.

    Args:
        filename (str): Is specified, use this filename.
            Otherwise $XDG_CACHE_HOME/addb.json is used.
    """
    if filename is not None:
        return filename

    return os.path.join(xdg_cache_home , 'addb.json')


def load_cache(filename=None):
    """
    Load cache file.

    Args:
        filename (str): cache filename. Is None, the XDG default path is used.

    Return: Cache content object (usually a dict or a list)
    """

    filename = _determine_cache_filename(filename)

    try:
        with open(filename, 'r') as fd:
            return json.load(fp)
    except FileNotFoundError:
        return {}


def save_cache(cache, filename=None):
    """
    Save cache file.

    Args:
        filename (str): cache filename. Is None, the XDG default path is used.
    """

    filename = _determine_cache_filename(filename)

    with open(filename, 'w') as fd:
        json.dump(cache, filename)