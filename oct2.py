from sys import setrecursionlimit, set_int_max_str_digits

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
setrecursionlimit(1000000024) 
set_int_max_str_digits(99999)
print(factorial(1000000))