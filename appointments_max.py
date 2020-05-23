#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countMeetings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY firstDay
#  2. INTEGER_ARRAY lastDay
#

def countMeetings(firstDay, lastDay):
    # Write your code here
    appoint=dict()
    max_ret=0
    for i in range(len(firstDay)):
        start=firstDay[i]
        end=lastDay[i]
        while start<=end:
            if start not in appoint.keys():
                appoint[start]=1
                max_ret+=1
                break
            start+=1
    return max_ret
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    firstDay_count = int(input().strip())

    firstDay = []

    for _ in range(firstDay_count):
        firstDay_item = int(input().strip())
        firstDay.append(firstDay_item)

    lastDay_count = int(input().strip())

    lastDay = []

    for _ in range(lastDay_count):
        lastDay_item = int(input().strip())
        lastDay.append(lastDay_item)

    result = countMeetings(firstDay, lastDay)

    fptr.write(str(result) + '\n')

    fptr.close()
