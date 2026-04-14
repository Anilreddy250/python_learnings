import argparse
class Solution:
    def twoSum(self, nums: list[int], target: int) :#-> list[int]:

#         # Dictionary to store: {value: index}
#         seen = {}
        
#         for index, num in enumerate(nums):
#             # Calculate the value we need to find
#             complement = target - num
            
#             # If the complement exists in our map, we found the pair!
#             if complement in seen:
#                 return [seen[complement], index]
            
#             # Otherwise, save the current number and its index
#             seen[num] = index
        
#         return []



# ... (Keep your class Solution: definition here)

        if __name__ == "__main__":
            # 1. Setup the CLI parser
            parser = argparse.ArgumentParser(description="Find two indices that sum to a target.")
            
            # 2. Define the parameters
            # nargs='+' allows you to pass multiple numbers as a list
            parser.add_argument("--nums", nargs='+', type=int, required=True, help="List of numbers")
            parser.add_argument("--target", type=int, required=True, help="The target sum")
            
            # 3. Parse and execute
            args = parser.parse_args()
sol = Solution()
result = sol.twoSum(args.nums, args.target)

print(f"Indices: {result}")
