#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'predictAnswer' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stockData
#  2. INTEGER_ARRAY queries
#

def predictAnswer(stockData, queries):
    # Write your code here
    tot_stck=len(stockData)
    ret=[]
    for q in queries:
        i=q-1-1
        j=q
        while i>=0 and stockData[i]>=stockData[q-1]:
            i-=1
        while j<tot_stck and stockData[j]>=stockData[q-1]:
            j+=1
        if i<0 and j>=tot_stck:
            ret.append(-1)
        elif i>=0 and j>=tot_stck:
            ret.append(i+1)
        elif i<0 and j<tot_stck:
            ret.append(j+1)
        else:
            i_dis=q-1-i
            j_dis=j-(q-1)
            if i_dis<=j_dis:
                ret.append(i+1)
            else:
                ret.append(j+1)
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stockData_count = int(input().strip())

    stockData = []

    for _ in range(stockData_count):
        stockData_item = int(input().strip())
        stockData.append(stockData_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = predictAnswer(stockData, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
