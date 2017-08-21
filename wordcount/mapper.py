#!/usr/bin/python
import sys


def mapper():
    for line in sys.stdin:
        data = line.strip().split(' ')
        for word in data:
            print "{0}\t{1}".format(word, 1)

if __name__ == "__main__":
    mapper()
