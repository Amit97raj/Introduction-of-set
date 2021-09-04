 # Python Basics Chapter 8:
# ========================

# 1. Introduction To Sets

# unordered collection of unique items
#  no order, no indexing, no duplicate values
# you can store number, string, tuple but you cant store list, set, 
# dict in sets.

# s = {1, 2, 3}
# print(s)

# s = {1, 2, 3, 2, 3, 1}
# print(s)

# l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8]

# remove duplicates -

# s = set(l)
# print(s)

# s = {1, 2, 3}

# s.add(4)
# print(s)

# s.remove(3)
# print(s)

# s.discard(3)
# print(s)

# s.clear()
# print(s)

# s_copy = s.copy()
# print(s_copy)

# 2. More About Sets

# in keyword in sets and for loop 

# s = {'a', 'b', 'c'}

# # in keyword to check if item is present or not in set

# if 'd' in s:
#     print('present')
# else:
#     print('not present')

# for loop

# for item in s:
#     print(item)

# set maths

# s1 = {1, 2, 3, 4}
# s2 = {3, 1, 4, 5, 6}

# union -

# s3 = s1.union(s2)
# print(s3)

# s3 = s1 | s2
# print(s3)

# intersection -

# s4 = s1.intersection(s2)
# print(s4)

# s4 = s1 & s2
# print(s4)
