#1. Timing function execution:Write a decorator the time function takes to execute

import time

def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        end_time= time.time()
        print(start_time)
        print(end_time)
        print(f"{func.__name__} ran in {end_time-start_time}")
        return func(*args,**kwargs)
    return wrapper

@timer
def some_func(n):
    time.sleep(n)

some_func(4)


#2. Debugging Function Calls:Create a Decorator to print the function name and the values of its arguments
# everytime the function is called....

def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(args) for arg in args)
        kwargs_values = ', '.join(f"{key}={value}" for key,value in kwargs.items())
        print(args_value)
        print(kwargs_values)
        print(f"calling:{func.__name__} with argsvalues:{args_value} and kwargsvalues:{kwargs_values}")
        return func(*args,**kwargs)
    return  wrapper

@debug
def hello():
    print("hello")
hello()

@debug
def some_func(name , greetigs="Namaste"):
    print(f"hello, {name}\n{greetigs}{'❤'}")

some_func('abinash',greetigs="Hare Krishn")

# 3.Cache Return Values:Implement a decorator that caches the return value of a function so that when it's called with the same arguments
#the cached value is returned instead of re-executing the function
import time

def cache(func):
    cache_values = {}
    print(cache_values)
    def wrapper(*args,**kwargs):
        if args in cache_values:
            return cache_values[args]
        result = func(*args,**kwargs)
        cache_values[args] = result
        return result
    return wrapper

@cache
def long_executing_function(a,b):
    time.sleep(3)
    return a+b

print(long_executing_function(2,3))
print(long_executing_function(2,3))
print(long_executing_function(4,6))

