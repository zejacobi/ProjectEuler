from os import path
from glob import glob

import argparse

parser = argparse.ArgumentParser(description='Helper to quickly run solution files')
parser.add_argument('-l', '--last', dest='last', action='store_true',
                    help='Runs the last solution')
parser.add_argument('-n', '--number', dest='number',
                    help='Runs the solution to the provided question number. Raises error if '
                         'missing; fills in any missing padding')

args = parser.parse_args()

if args.last:
    options = sorted([path for path in glob('.' + path.sep + 'Solutions' + path.sep + '*')
                      if '__' not in path])

    last = options[-1]

    last_name = last.split(path.sep)[-1].split('.')[0]
    __import__('Solutions.' + last_name)
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
    __import__('Solutions.' + number)