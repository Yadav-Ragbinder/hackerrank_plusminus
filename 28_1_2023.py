import math
import os
import random
import re
import sys

def plusMinus(arr):
    neg = 0
    pos = 0
    zer = 0
    length = len(arr)
    for i in range(length):
        if arr[i]<0:
            neg=  neg + 1
        elif arr[i]>0:
            pos = pos + 1
        else:
            zer =  zer + 1
    positive = int(pos/n)
    negtive = int(neg/n)
    zero = int(zer/n)
    print(f"The first 5 digits of positive are {positive:.5f}")
    print(f"The first 5 digits of negtive are {negtive:.5f}")
    print(f"The first 5 digits of zero are {zero:.5f}")            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
