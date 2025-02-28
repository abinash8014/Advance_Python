#LIST COMPREHENSION ::::
#1. i want 'n' for each 'n' in nums
from idlelib.colorizer import prog_group_name_to_tag
from idlelib.debugobj import myrepr

# nums = [1,2,3,4,5,6,7,8,9,10]
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# Using List comprehension:
# my_list=[n for n in nums]
# print(my_list)

#2. I want n*n for each 'n' in nums
# my_list=[]
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# Using list comprehension
# my_list=[n*n for n in nums]
# print(my_list)

# Using a map+lambda
# my_list = map(lambda n: n*n,nums)
# print(my_list)

# 4.I want n for each n in nums if n is even
# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)

# Using List comprehension
# my_list = [n for n in nums if n%2==0]
# print(my_list)

# Using filter and lambda function
# my_list = filter(lambda n:n%2==0,nums)
# print(my_list)

#5. I want a (letter,num) pair for each in 'abcd' and each number in '0123'
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)

# Using a list comprehension
# my_list=[(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# DICTIONARY COMPREHENSION:::::
# names = ['abinash','deepak','anu','saumya','smaraki']
# heroes = ['Thor','Superman','Deadpool','wolverine','Dstrange']
# print(list(zip(names,heroes)))

# my_dict = {}
# for name,hero in zip(names,heroes)

# exclude the name abinash with his hero
# my_dict = {name:hero for name,hero in zip(names,heroes) if name != 'abinash'}
# print(my_dict)

# SET COMPREHENSION::::
# numbers = [1,1,2,1,3,4,5,6,5,6,3,5,5,6,7,7,8,9,9,8]
# my_set = set()
# for n in numbers:
#     my_set.add(n)
# print(my_set)

# Using the set comprehension
# my_set = {n for n in numbers }
# print(my_set)