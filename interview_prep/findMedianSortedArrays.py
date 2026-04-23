# def findMedianSortedArrays(nums1, nums2):
#     # Ensure nums1 is the smaller array to optimize binary search range
#     if len(nums1) > len(nums2):
#         nums1, nums2 = nums2, nums1
        
#     m, n = len(nums1), len(nums2)
#     low, high = 0, m
    
#     while low <= high:
#         partition1 = (low + high) // 2
#         # Calculate partition2 such that left and right halves are balanced
#         partition2 = (m + n + 1) // 2 - partition1
        
#         # Handle edge cases where partitions are at the very beginning or end
#         l1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
#         r1 = nums1[partition1] if partition1 < m else float('inf')
        
#         l2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
#         r2 = nums2[partition2] if partition2 < n else float('inf')
        
#         if l1 <= r2 and l2 <= r1:
#             # Correct partition found
#             if (m + n) % 2 == 0:
#                 return (max(l1, l2) + min(r1, r2)) / 2.0
#             else:
#                 return max(l1, l2)
#         elif l1 > r2:
#             # Move partition1 to the left
#             high = partition1 - 1
#         else:
#             # Move partition1 to the right
#             low = partition1 + 1

# print(findMedianSortedArrays([1,2,3],[4,5,6,7]))
    

###########################
#short way to do 

class Solution:
    # 1. Added 'self' as the first parameter
    def findMedianSortedArrays(self, nums1, nums2):
            
        merged = sorted(nums1 + nums2)
        length = len(merged)
        mid = length // 2

        if length % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2.0
        
        return float(merged[mid])

nums1 = [1, 2, 3, 4, 5]
nums2 = [7, 8, 9]

results = Solution()
ans = results.findMedianSortedArrays(nums1, nums2)

# 2. Fixed the f-string formatting to actually print the variable
print(f"the median of two given list is : {ans}")