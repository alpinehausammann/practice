#!/bin/python3

import sys


n = int(input().strip())
arr = [ arr_temp for arr_temp in str(input()).strip().split(' ')]

for i in range(len(arr), len(arr)-n, -1):
    print("{} ".format(arr[i-1]), end='')