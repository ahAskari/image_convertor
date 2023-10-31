#!/usr/bin/env python3
from convertor import cli_handler, conversion


if __name__ == '__main__':
    fmt = cli_handler().format
    path = cli_handler().path
    quality = cli_handler().quality
    size = cli_handler().size

    conversion(fmt, path, quality, size)
