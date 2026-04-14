# def rotate(nums, k):
#     n = len(nums)
#     if n ==0:
#         return nums
#     k = k%n
#     return nums[-k:] + nums[:-k]

# print(rotate([1,2,3,4,5],2))
# print(rotate([1,2,3,4,5],7))
# print(rotate([1,2,3,4,5],1))
nums = [1,2,3,4,5]

def rotate(nums,k):

    n = len(nums)
    if n==0:
        return #nums
    k = k%n
    def reverse(lst, left, right):
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left +=1
            right -=1
    print(reverse(nums,0, n-1))
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)

    rotate(nums,2)
    print(nums)