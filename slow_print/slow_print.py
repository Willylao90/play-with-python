#!/usr/bin/python

''' Module for printing slowly like the 80's style '''

import time
import random
import sys

def slowprint(string):
   ''' Slow print function '''
   for char in string:
      time.sleep(0.05 * random.random())
      print(char, end='', flush=True)


if __name__=='__main__':
   for line in sys.stdin:
      slowprint(line)
