"""
Because of a decision by Guido, it's hard to run scripts directly from a sub-directory of a python
project if they have imports. I understand why he decided this, but it was a bit of a pain when I
wanted to abstract out some functions to a separate library file. That meant I had to make a runner.

Unfortunately, I didn't want to change anything I'd already done, so this file does some stuff I
know is bad, like importing files based on a programatic determination of their name and trusting
that to be all you need to run them, and printing time via an exit handler (because many of my
solutions call `exit()` as soon as they're done). It's a bit ugly but it gets the job done and
makes my life a bit easier while I'm developing new solutions.
"""

from os import path
from glob import glob
import time
import atexit

import argparse

parser = argparse.ArgumentParser(description='Helper to quickly run solution files')
parser.add_argument('-l', '--last', dest='last', action='store_true',
                    help='Runs the last solution')
parser.add_argument('-t', '--time', dest='time', action='store_true',
                    help='Outputs the time the program takes to run')
parser.add_argument('-n', '--number', dest='number',
                    help='Runs the solution to the provided question number. Raises error if '
                         'missing; fills in any missing padding')

args = parser.parse_args()

if args.last:
    options = sorted([file_path for file_path in glob('.' + path.sep + 'Solutions' + path.sep + '*')
                      if '__' not in file_path])

    last = options[-1]

    number = last.split(path.sep)[-1].split('.')[0]
elif args.number:
    number = args.number
    while len(number) < 4:
        number = '0' + number
    number_file = number + '.py'
    sol_path = path.join('.', 'Solutions', number_file)
    try:
        open(sol_path, 'r')
    except FileNotFoundError:
        print('Error: Solution "{}" does not exit'.format(number))
        exit(1)
else:
    print('No arguments provided; closing.')
    exit()

if args.time:
    start = time.time()

    # we use exit() in a bunch of places. So we need to register an exit function to print the time
    def print_time():
        if args.time and start:
            end = time.time()
            run = end - start
            print('Solution took: {:.4f}s'.format(run))

    atexit.register(print_time)

__import__('Solutions.' + number)


