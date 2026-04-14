def twoSumBruteForce(nums, target):
    for i in range(len(nums)): # First pointer
        for j in range(i + 1, len(nums)): # Second pointer (starts after i)
            if nums[i] + nums[j] == target:
                print(i, j)
                return [i, j]
            print(i, j)
            
    return []
# print(i, j)