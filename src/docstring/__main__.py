"""

Doc string generator
"""
import argparse
import os

from docstring import parse


def generator_source(src: list):
    for item in src:
        if os.path.isfile(item):
            yield item
        elif os.path.isdir(item):
            for root, _dirs, files in os.walk(item):
                for filepath in files:
                    yield os.path.join(root, filepath)


def main():
    _parser = argparse.ArgumentParser("docstring")
    _parser.add_argument("src", action="append")
    _args = _parser.parse_args()

    for _path in generator_source(_args.src):
        with open(_path, "r") as _file:
            try:
                print(parse(_file.read(), _path))
            except Exception as err:
                print(f"fail to parse {_path} {type(err)} {err}")


if __name__ == "__main__":
    main()
