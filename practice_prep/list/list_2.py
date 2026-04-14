# my_list = ["a","b","c","c","d","d"]
# unique_list = list(set(my_list))
# unique_list.sort()
# print(unique_list)


import copy
a = [[1,2],[3,4]]
b = a.copy() # shallow
b[0][0] = 99 # also chanes a!


c=copy.deepcopy(a) # deep copy
c[0][0] = 88 #a is unaffected
print(a)
print(b)
print(c)