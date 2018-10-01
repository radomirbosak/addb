#!/usr/bin/env python3

from .__version__ import __version__
from .cli import parse_args


def main():
    args = parse_args()

    if args.version:
        print(f'addb {__version__}')


if __name__ == '__main__':
    main()
