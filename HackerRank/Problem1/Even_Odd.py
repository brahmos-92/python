# HackerRank code problem 1 for python Solved
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip());
    if n^1 == (n+1):
  #      print("Even");
        if n in range(2,6,1):
            print("Not Weird");
        elif n in range(6,21,1):
            print("Weird");
        else:
            print("Not Weird");
    else:
        print("Weird");
