from math import sqrt

def check_if_prime(num):
    if num==2:
        return True
    if num%2==0:
        return False
    i=3
    while i<= sqrt(num):
        if num%i==0:
            return False
        i+=2
    return True

def manipulate_generator(g,n):
    i=n+1
    while check_if_prime(i):
        #print("I: ",i)
        #print("G: ",next(g))
        next(g)
        i+=1
        

def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1

k = int(input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n) 
    manipulate_generator(g, n)
