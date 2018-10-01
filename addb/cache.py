# -*- coding: utf-8 -*-

import os
import json

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
            return json.load(fd)
    except FileNotFoundError:
        return new_cache()


def save_cache(cache, filename=None):
    """
    Save cache file.

    Args:
        filename (str): cache filename. Is None, the XDG default path is used.
    """

    filename = _determine_cache_filename(filename)

    with open(filename, 'w') as fd:
        json.dump(cache, fd, indent=4, sort_keys=True)


def new_cache():
    """
    Generate a new cache object with empty structure

    Return: cache dict
    """
    return {"anime": []}


def find_anime(name_or_alias, cache):
    existing_names = {}
    for anime in cache['anime']:
        existing_names[anime['name']] = anime
        for alias in anime.get('alias', []):
            existing_names[alias] = anime

    return existing_names.get(name_or_alias)
