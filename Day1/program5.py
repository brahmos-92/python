# Odd and Even program
import math
import os
import random
import re
import sys

def evenOdd1(number):
  if (n&1 == 1):
    print("Odd")
  else:
    print("Even")

def evenOdd2(number):
    if (n%2 == 0):
        print("Even")
    else:
        print("Odd")

if __name__ == '__main__':
    n = int(input().strip())
    evenOdd1(n)
    evenOdd2(n)
