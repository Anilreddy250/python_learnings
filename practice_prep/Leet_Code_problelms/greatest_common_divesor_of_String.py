# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         self.str1 = "ABCABC"#str1
#         self.str2 = "ABC"#str2
#         str3 =""

#         for i,j in zip(str1, str2):                                  
#                             if i==j:
#                                 str3 += i
#                                 print(str3)
#                                 # return str3
#                             else: 
#                                     print("i is not equal to j")

# import math

# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         # Step 1: Check if a common divisor even exists
#         if str1 + str2 != str2 + str1:
#             return ""
        
#         # Step 2: Find the GCD of the lengths
#         # Example: len("ABCABC") is 6, len("ABC") is 3. GCD is 3.
#         max_length = math.gcd(len(str1), len(str2))
        
#         # Step 3: Return the prefix of that length
#         return str1[:max_length]
# ans = Solution()
# # results = ans.gcdOfStrings("ABCABC", "ABC")
# results = ans.gcdOfStrings(str1="ABCABC", str2="ABC")

# print(results)

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Step 1: Logic check - If they don't share a pattern, 
        # combining them in different orders will result in different strings.
        if str1 + str2 != str2 + str1:
            return ""

        # Step 2: Manually find the GCD of the lengths
        # We use the Euclidean Algorithm: gcd(a, b) = gcd(b, a % b)
        a = len(str1)
        b = len(str2)
        while b:
            a, b = b, a % b
        
        # 'a' is now the Greatest Common Divisor of the two lengths
        return str1[:a]
ans = Solution()
# results = ans.gcdOfStrings("ABCABC", "ABC")
results = ans.gcdOfStrings(str1="ABCABC", str2="ABC")
