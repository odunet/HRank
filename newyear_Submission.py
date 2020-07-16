#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    if len(q) >= 3:
        iter = 3
        for i in range(len(q)):
            if  q[i]>=(i-iter) and q[i]<=(i+iter):
                pass
            else:
                print('Too chaotic')
                return 0

        z = 0
        for j in range(len(q),0,-1):
            if q[j-1] == j:
                 continue
            for i in range(len(q)-1,-1,-1):
                if j == q[i]:
                    if j-1-i>1:
                        z += 2
                        q[i],q[j-1] = q[j-1],q[i]
                        q[i],q[i+1] = q[i+1],q[i]
                    else:
                        z += 1
                        q[i],q[j-1] = q[j-1],q[i]
        print(z)
#Not necessary, could be removed
    else:
        if q[0] == 1 and q[1] == 2:
            print(0)
        else:
            q[0], q[1] = q[1], q[0]
            print(1)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
