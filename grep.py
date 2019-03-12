#!/usr/bin/python3
import re
import argparse


def search_it(params):
    mode = params.mode
    pattern = params.pattern
    filename = params.file

    with open(filename, 'r') as file:
        if pattern.startswith('^'):
            return search_regexp(pattern, file, mode)
        else:
            return search_string(pattern, file, mode)


def read_file(file):
    while True:
        string = file.readline()
        if not string:
            break
        yield string


def search_string(string, file, mode):
    result = []
    for line in read_file(file):
        if mode:
            if re.search(string, line):
                result.append(line)
        else:
            if not re.search(string, line):
                result.append(line)
    return result


def search_regexp(pattern, file, mode):
    result = []
    for line in read_file(file):
        if mode:
            if re.match(pattern, line):
                result.append(line)
        else:
            if not re.match(pattern, line):
                result.append(line)
    return result


def main(input_args):
    result = search_it(input_args)

    for line in result:
        print(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--mode', action='store_false', help='Exclude string from search result')
    parser.add_argument('pattern', action='store', help='Search pattern')
    parser.add_argument('file', action='store', help='File fo search')
    args = parser.parse_args()
    main(args)
