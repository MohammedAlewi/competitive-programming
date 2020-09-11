#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    indexs = [0]*110

    for val in arr:
        indexs[ int(val[0]) ] +=1
    
    for i in range(1,len(indexs)):
        indexs[i]+=indexs[i-1]

    result= [""]*len(arr)

    for i in range(len(arr)-1,-1,-1):
        indexs[ int(arr[i][0]) ] -=1
        if i < len(arr)//2:
            result[ indexs[ int(arr[i][0]) ] ] = "-"
        else:
            result[ indexs[ int(arr[i][0]) ] ] = arr[i][1]

    print(" ".join(result))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
