#!/usr/bin/python

import argparse


def find_max_profit(prices):
  # start with initial value incase all are negative profits (<0)
    max_profit = prices[1] - prices[0]
    # loop through prices
    for i in range(len(prices)):
        print(f'OUTER LOOP: {i}')
        # grab first price and compare to each BEFORE it
        for j in range(i):
            print(
                f'    INNER LOOP: {j} --- {prices[i]} - {prices[j]} =  {prices[i] - prices[j]}  --- {max_profit}')
            if prices[i] - prices[j] > max_profit:
                # save max difference
                max_profit = prices[i] - prices[j]

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
