#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import webbrowser

from .__version__ import __version__
from .cli import parse_args
from .cache import load_cache, find_anime, save_cache
from .common import get_now_utc, get_min_utc, update_episode_urls
from .list_db import list_db
from .add import add


def export(args):
    cache = load_cache(args.cache)
    print(json.dumps(cache, indent=4, sort_keys=True))


def watch(args):
    cache = load_cache(args.cache)
    anime = find_anime(args.name, cache)
    if anime is None:
        print('Anime not found.')
        sys.exit(1)
    elif not anime.get('watch_url'):
        print('There is no watch url associated with this anime.')
        sys.exit(1)

    # support custom episode-based urls
    url = anime['watch_url']
    if 'episode_url' in anime:
        episode_urls = anime['episode_url']
        next_episode = anime["progress"] + 1
        if len(episode_urls) >= next_episode:
            url = episode_urls[next_episode - 1]

    print(f'Last watched episode: {anime["progress"]}')
    webbrowser.open(url)


def remove(args):
    cache = load_cache(args.cache)
    anime = find_anime(args.name, cache)
    if anime is None:
        print('Anime not found.')
        sys.exit(1)

    cache['anime'].remove(anime)

    save_cache(cache, args.cache)


def update(args):
    cache = load_cache(args.cache)
    anime = find_anime(args.name, cache)
    if anime is None:
        print('Anime not found.')
        sys.exit(1)

    if args.episode is None:
        anime['progress'] += 1
    else:
        anime['progress'] = int(args.episode)

    # update modify date
    anime['last_updated_at'] = get_now_utc().isoformat()

    anime_name = anime['full_name'] or anime['name']

    print(f'Anime/drama "{anime_name}" is now at episode {anime["progress"]}')

    save_cache(cache, args.cache)


def edit(args):
    cache = load_cache(args.cache)
    anime = find_anime(args.name, cache)

    if anime is None:
        print('Anime not found.')
        sys.exit(1)

    if args.alias is not None:
        anime['alias'] = args.alias
        print('Aliases changed to: ' + ', '.join(args.alias))

    if args.status is not None:
        anime['status'] = args.status
        print(f'Status changed to: {args.status}')

    if args.full_name is not None:
        anime['full_name'] = args.full_name
        print(f'Full name changed to: {args.full_name}')

    if args.watch_url is not None:
        anime['watch_url'] = args.watch_url
        print(f'Watch url changed to: {args.watch_url}')

    if args.update_episode_urls:
        update_episode_urls(anime)

    save_cache(cache, args.cache)


def main():
    """
    Main program entry point

    Parse arguments and run the corresponding action
    """

    # parse normal arguments
    args = parse_args()

    if args.version:
        print(f'addb {__version__}')
        sys.exit(0)
    elif args.action == 'export':
        export(args)
    elif args.action == 'add':
        add(args)
    elif args.action == 'watch':
        watch(args)
    elif args.action == 'remove':
        remove(args)
    elif args.action == 'update':
        update(args)
    elif args.action == 'edit':
        edit(args)
    elif args.action in ['list', None]:
        if args.action is None:
            args.status = 'watching'
        list_db(args)


if __name__ == '__main__':
    main()
