#!/bin/python3

import math
import os
import random
import re
import sys

def minimumBribes(q):
    if len(q) >= 3:
        iter = 3
        #Checkif chaotic or not
        for i in range(len(q)):
            print(q[i],i-iter,i+iter)
            if  q[i]>=(i-iter) and q[i]<=(i+iter):
                print('The list is  Not Chaotic')
                pass
            else:
                print('The list is  Chaotic')
                return 0

        #loop round to see were index exist in the list
        z = 0
        for j in range(len(q),0,-1):
            if q[j-1] == j:
                 print(i, q[j-1]," Test i")
                 continue
            for i in range(len(q)-1,-1,-1):
                if j == q[i]:
        #switch the list item and increament counter
                    if j-1-i>1:
                        z += 2
                        q[i],q[j-1] = q[j-1],q[i]
                        q[i],q[i+1] = q[i+1],q[i]
                    else:
                        z += 1
                        q[i],q[j-1] = q[j-1],q[i]
        print(q,' and the number of bribes necessary is: ',z)

    #run this is list has less than three item
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
        q = list(map(int, input().split()))
        minimumBribes(q)
