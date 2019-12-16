#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    possibilites = []

    def inner(n, possibilites):
        if n == 0:
            return [possibilites]

        return inner(n-1, possibilites + ['rock']) + inner(n-1, possibilites + ['paper']) + inner(n-1, possibilites + ['scissors'])

    return inner(n, possibilites)


print(rock_paper_scissors(5))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
