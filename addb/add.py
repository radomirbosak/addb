# -*- coding: utf-8 -*-

import sys
from itertools import chain

from .cache import load_cache, save_cache
from .common import get_now_utc


def add(args):
    cache = load_cache(args.cache)

    # check if there's isn't an anime with the same name already in DB
    if _check_conflict(args.name, args.alias, cache['anime']):
        print(f'Error: The provided name/alias is already used!')
        sys.exit(1)

    nowstr = get_now_utc().isoformat()

    # no name conflict, let's move on
    new_entry = {
        "name": args.name,
        "alias": args.alias,
        "status": args.status,
        "progress": 0,
        "full_name": args.full_name,
        "watch_url": args.watch_url,
        "created_at": nowstr,
        "last_updated_at": nowstr,
    }

    cache['anime'].append(new_entry)

    save_cache(cache, args.cache)


def _check_conflict(new_name, new_alias, cache_anime):
    existing_names = {}
    for anime in cache_anime:
        existing_names[anime['name']] = anime
        for alias in anime.get('alias', []):
            existing_names[alias] = anime

    name_occupied = new_name in existing_names
    alias_occupied = any(alias in existing_names for alias in new_alias)
    return name_occupied or alias_occupied
