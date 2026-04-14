# list = [1,2,4,5]
def sum(lst, target):
    n =len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i]+lst[j] ==target:
                return [i, j]
    return 1
lst = [1,2,4,5]
target = 6
print(sum(lst,target))



# binary_search-----------------------------------------------8888888-----------------
def binary_search(lst, low, high, x):
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def two_sum_binary(lst, target):
    for i in range(len(lst)):
        # The number we are looking for to complete the sum
        complement = target - lst[i]
        
        # Search for 'complement' in the REST of the list (i+1 onwards)
        index = binary_search(lst, i + 1, len(lst) - 1, complement)
        
        if index != -1:
            return [i, index]
            
    return None # Return None if no pair is found

# Test
nums = [1, 2, 4, 5]
goal = 6
print(two_sum_binary(nums, goal)) # Output: [1, 2] (because 2 + 4 = 6)