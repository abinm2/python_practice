#!/bin/python

import math
import os
import random
import re
import sys

def consumer():
    while True:
        x = yield
        print(x)

def producer(n):
    for _ in range(n):
        x = int(input())
        print("prod: ",x)
        yield x


# Complete the 'rooter', 'squarer', and 'accumulator' function below.

def rooter():
    # Write your code here
    while True:
        x=yield 
        yield math.sqrt(x)

def squarer():
    # Write your code here
    while True:
        x=yield
        print("sqr: ",x)
        yield (x*x)

def accumulator():
    # Write your code here
    current_sum=0
    while True:
        x=yield
        print("acc: ",x)
        y=current_sum+x
        current_sum=y
        yield y

def pipeline(prod, workers, cons):
    for num in prod:
        for i, w in enumerate(workers):
            print("i,w: ",i,w)
            num = w.send(num)
            w.send(None)
        cons.send(num)
    for worker in workers:
        worker.close()
    cons.close()


if __name__ == '__main__':
    order = input().strip()
    print("Order: ",order)
    n = int(input())

    prod = producer(n)

    cons = consumer()
    next(cons)
    
    root = rooter()
    next(root)

    accumulate = accumulator()
    next(accumulate)

    square = squarer()
    next(square)

    pipeline(prod, eval(order), cons)
