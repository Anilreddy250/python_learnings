def sum(lst, target):
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            # if lst[i] + lst[j] == target:
            if i + j == target:
                return [i, j]
    return 1
lst = [1,2,4,5]
target = 3
print(sum(lst,target))

# ---------binary_code-------------
def binary_search(lst,low, high,x):
    while low <= high:
        mid = (low + high) //2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x :
            low = mid +1
        else:
            high = mid - 1
    return -1
def two_sum_binary(lst, target):
    for i in range(len(lst)):
        pass