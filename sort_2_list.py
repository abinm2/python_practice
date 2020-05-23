list1 = [1, 2, 5, 4, 4, 3, 6]
list2 = [3, 2, 9, 7, 10, 7, 8]

def ret_diff(x):
    return x[1]-x[0]

x = sorted(zip(list1,list2),key=ret_diff)

for i in x:
    print(i)



