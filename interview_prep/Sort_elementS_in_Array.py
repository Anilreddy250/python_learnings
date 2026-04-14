# bubble sort:
# this is the simplest (and least efficient) sort. it repeatedly steps though the list, compares adhacent elements, and  swaps them if they are in order?
# base case: O(n)(if already sorted)
# worstcase O(n^2)
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped  = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j +1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if not swapped :
#             break
# #     return arr
# thelist = ["a" ,"b"]
# for i , j in enumerate(thelist):
    # print(i,j)
    # __str__(i, j)
# import gc
# # Manually trigger a garbage collection

# results = gc.collect()
# print(results)