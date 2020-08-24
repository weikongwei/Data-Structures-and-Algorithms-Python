# Method 1: recursion + memoization (Top-down)
# Outer function is a closure to hold cache

import time

def fib_outer():
    cache = {}

    # Inter function is to do calculations
    def fib(n):
        if n <= 1:
            return n
        if n not in list(cache.keys()):
            cache[n] = fib(n - 1) + fib(n - 2)
            # print(cache)
        return cache[n]

    return fib

num = 50
start = time.time()
f = fib_outer()
print("Recursion + memoization:",f(num))
print("Time used: " , time.time() - start)


#################################
# Method 2: bottom up (iteration)

def fib(n):
  result = [0,1]

  for i in range(2,n+1):
    result.append(result[i-1]+result[i-2])

  return result[-1]

start = time.time()
f = fib(num)
print("Bottom-up:", f)
print("Time used: " , time.time() - start)







# Solution

# from functools import lru_cache
#
# @lru_cache(maxsize = 1000)
# def fib(n):
#   if n < 2:
#     return n
#   else:
#     return fib(n-1) + fib(n-2)
#
# print(fib(10))
# print(fib.cache_info())
#
#
# cache = {}
#
# def fibo(n):
#   if n in cache:
#     return cache[n]
#   elif n < 2:
#     cache[n] = n
#     return cache[n]
#   else :
#     cache[n] = fib(n-1) + fib(n-2)
#
#     return cache[n]
#
#
# x = fibo(8)
# print(cache)
# print(x)
