# lambda expression :: single line function is called as lambda fucntion.
"""
lambda a,b : a + b
lambda a,b : a - b
lambda a : a * a
"""
# a = lambda a , b: a + b
# b = a(20, 30)
# print(b)

# map ::  will adds the given condition
num = [10,203,20121,3234,321342,212,11121,9921929]
a = list(map(lambda num : num + num, num))
print(a)

# filter :: its filter the given condition
b = list(filter(lambda num : num% 2!=0, num))
print(b)

# reduce :: will add or multiple and gives the output in one
from functools import reduce
c = reduce(lambda a ,b : a + b, num)
print(c)