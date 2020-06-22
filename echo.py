#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Corbin Creech"


import sys
import argparse


def to_upper(text):
    result = text.upper()
    return result

def to_lower(text):
    result = text.lower()
    return result

def to_title(text):
    result = text.title()
    return result

def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        'text', help='text to be manipulated'
    )
    parser.add_argument(
        "-u", "--upper", action='store_true', help="convert text to uppercase"
    )
    parser.add_argument(
        "-l", "--lower", action='store_true', help="convert text to lowercase"
    )
    parser.add_argument(
        "-t", "--title", action='store_true', help="convert text to titlecase"
    )
    return parser


def main(args):
    """Implementation of echo"""

    parser = create_parser()
    ns = parser.parse_args(args)

    text = ns.text
    upper = ns.upper
    lower = ns.lower
    title = ns.title

    if title:
        print(to_title(text))
    elif lower:
        print(to_lower(text))
    elif upper:
        print(to_upper(text))
    else:
        print(text)

    


if __name__ == '__main__':
    main(sys.argv[1:])
