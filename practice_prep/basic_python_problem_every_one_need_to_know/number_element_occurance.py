my_list = [1,2,2,2,3,3,3,4,4,4,4,4,5,5,5,6,6,6,6]
# counts ={}
# for item in my_list:
#     if item in counts:
#         counts[item] += 1
#     else:
#         counts[item] = 1
# print(counts)


from collections import Counter
counts = Counter(my_list)
print(counts)

counts = {x: my_list.count(x) for x in set(my_list)}
print(counts)
