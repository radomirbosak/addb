#!/usr/bin/env python3

import sys
import json


from .__version__ import __version__
from .cli import parse_args
from .cache import load_cache
from .list_db import list_db


def export(args):
    cache = load_cache(args.cache)
    print(json.dumps(cache, indent=4, sort_keys=True))


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
    elif args.action in ['list', None]:
        list_db(args)


if __name__ == '__main__':
    main()
