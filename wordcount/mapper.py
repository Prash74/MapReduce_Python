#!/usr/bin/python
import sys


def mapper():
    for line in sys.stdin:
        date = line.strip().split(',')[1]
        year = date.split('-')[0]
        print "{0}\t{1}".format(year, 1)

if __name__ == "__main__":
    mapper()
