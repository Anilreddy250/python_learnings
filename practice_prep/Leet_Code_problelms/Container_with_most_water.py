class Solution:
    def maxArea(self, height:list[int]) -> int:
        left, right = 0, len(height) - 1
        max_val = 0
        
        while left < right:
            # Calculate current area
            current_area = min(height[left], height[right]) * (right - left)
            max_val = max(max_val, current_area)
            
            # Move the pointer of the shorter wall
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return print(max_val)
    
ans = Solution()
results =ans.maxArea([1,2,3,4,5,9,5,4,3,2,1,8])
