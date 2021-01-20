from argparse import ArgumentParser
from pkgutil import iter_modules
from pathlib import Path

from bitbitbot import parsers


run_path = Path()
parser = ArgumentParser(
    prog='bitbitbot',
    description='A command line interface for the BitBitBot Twitch Chat Bot',
)
parser.set_defaults(func=lambda __: parser.print_help())
subparsers = parser.add_subparsers(help='commands')

for __, name, __ in iter_modules(parsers.__path__, f'{parsers.__name__}.'):
    __import__(name, fromlist=['_trash'])

parsers.load_subparsers(subparsers)


def main():
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
