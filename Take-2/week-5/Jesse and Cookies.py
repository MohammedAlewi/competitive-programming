#!/bin/python3

import os
import sys
import heapq
#
# Complete the cookies function below.
#
def cookies(k, A):
    heapq.heapify(A)
    counter = 0

    while k > A[0]:
        if len(A) < 2:
            return -1
        
        counter+=1

        fst,snd = heapq.heappop(A), heapq.heappop(A)
        heapq.heappush( A, fst * 1 + snd * 2 )

    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
