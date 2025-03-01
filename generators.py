# GENERATOR EXPRESSIONS::::

# 1.I want to yield 'n*n' for each n in nums
# nums = [1,2,3,4,5,6,7,8,9,10]

# Using Generator Expression
# def gen_function(nums):
#     for n in nums:
#         yield n*n
# my_gen = gen_function(nums)
# for i in my_gen:
#     print(i)

# generator expression
# my_gen = (n*n for n in nums)
# print(my_gen)

# 2.Square of list of numbers
# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     print(result)
#
# square_numbers([1,2,3,4,5])

# Generator
def square_numbers(nums):
    for i in nums:
        yield i*i
my_nums = square_numbers([1,2,3,4,5])
# print(next(my_nums))

for num in my_nums:
    print(num)

# Using generator comprehension
# my_gen = (i*i for i in [1,2,3,4,5])
# print(list(my_gen))

import random
import time
import memory_profiler

names = ['abinash','Deepak','Anu','Saumya','Smaraki']
majors = ['math','chemistry','biology','it','History']

print('Memory(Before):{}Mb'.format(memory_profiler.memory_usage_resource()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person={
            'id':1,
            'name':random.choice(names),
            'majors':random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person={
            'id':i,
            'name':random.choice(names),
            'majors':random.choice(majors)
        }
        yield person
t1 = time.perf_counter()
people=people_list(1000000)
t2=time.perf_counter()

# t1 = time.perf_counter()
# people=people_generator(1000000)
# t2=time.perf_counter()

print('Memory(after):{}Mb'.format(memory_profiler.memory_usage_resource()))
print('Took {} seconds'.format(t2-t1))