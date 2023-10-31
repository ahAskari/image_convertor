#!/usr/bin/env python3
import argparse

default_quality = 75
default_format = 'jpeg'


def cli_handler():
    parser = argparse.ArgumentParser(prog='convert', usage="convert [...Options]")

    parser.add_argument('--path', '-p', type=str, required=True, metavar='P')
    parser.add_argument('--format', '-f', type=str, metavar='E', default=default_format,
                        choices=['jpeg', 'png', 'webp'])
    parser.add_argument('--quality', '-q', type=int, metavar='Q', default=default_quality)
    parser.add_argument('--size', '-s', type=int, metavar='S')

    args = parser.parse_args()
    return args
