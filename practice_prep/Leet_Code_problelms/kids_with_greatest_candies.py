class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # Step 1: Find the current maximum candies in the group
        max_candies = max(candies)
        
        # Step 2: Create a result list by comparing (current + extra) to max_candies
        result = []
        for candy in candies:
            # Check if this kid could become the leader
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result

ans = Solution()
results = ans.kidsWithCandies([2,3,5,1,3], 3)
print(results)