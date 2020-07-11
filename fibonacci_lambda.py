#Fibonacci series using lambda and map
def fib(count):
    series = [0,1]
    any(map(lambda x: series.append(sum(series[-2:])),range(2,count)))
    return series[:count]


num = int(input("Enter the limit: "))
print(fib(num))


#Fibonacci series using lambda and reduce
from functools import reduce
fib_series = lambda n: reduce(lambda x,_: x+[x[-1]+x[-2]],range(n-2),[0,1])


count = int(input("Enter the limit: "))
print(fib_series(count))