#!/bin/python3

'''
boilerplate for python CLI scripts

@author: n00py <purplem@protonmail.com>
'''

import argparse, sys

parser = argparse.ArgumentParser(description='this is a general description of the purpose of this file')
parser.add_argument('number', metavar='N', type=int, help='just a number required to pass as arg')
args = parser.parse_args()


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def main(n):
	try:
		print(f"{bcolors.OKGREEN}Alright, colored output as well!{bcolors.ENDC}")
	except KeyboardInterrupt:
		print("\nBye")
		sys.exit()

if __name__ == "__main__":
	main(args.number)
