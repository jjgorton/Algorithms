#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # new_cache = cache

    # if n <= 1:
    #     return 1
    # if n == 2:
    #     return 2
    # if n == 3:
    #     return 4
    # if cache != None and n not in cache:
    #     new_cache[n] = (eating_cookies(n-1, new_cache) +
    #                     eating_cookies(n-2, new_cache) + eating_cookies(n-3, new_cache))
    #     print(new_cache)
    #     return new_cache[n]
    # else:
    #     return (eating_cookies(n-1) +
    #             eating_cookies(n-2) + eating_cookies(n-3))

    if n <= 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    n_1 = 1
    n_2 = 2
    n_3 = 4

    for _ in range(n-3):
        cur = n_1 + n_2 + n_3
        print(cur, n_1, n_2, n_3)

        n_1 = n_2
        n_2 = n_3
        n_3 = cur

    return cur


print(eating_cookies(5))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
