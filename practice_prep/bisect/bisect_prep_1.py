import bisect
# # @a sorted list of high scores
# scores = [100, 250, 400, 550, 800]
# new_score = 450
# position = bisect.bisect(scores, new_score)
# print(f"the new score should be at index:{position}")
# #actually insert it
# bisect.insort(scores, new_score)
# print(f"Upload leaderboard: {scores}")

# def get_grade(score):
#     breakpoints = [60,70,80,90]
#     grades = 'FDCBA'
#     i = bisect.bisect(breakpoints, score)
#     return grades[i]
# print(get_grade(85))
# print(get_grade(55))

# ___________________________________
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res = ""
#         n = len(s)
#         for i in range(n):
#             for char in s:
#                 if char[i] != char[i+1]:
#                     res += char
#         print(res)
# results = Solution()
# ans = results.lengthOfLongestSubstring(s="abcabcbb")
# +++++++++++++++++++++++++++++

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         char_set = set()
#         left = 0
#         max_length = 0
        
#         # 'right' moves across the string to expand the window
#         for right in range(len(s)):
#             # If we find a duplicate, shrink the window from the left
#             while s[right] in char_set:
#                 char_set.remove(s[left])
#                 left += 1
            
#             # Add the current character and update max_length
#             char_set.add(s[right])
#             max_length = max(max_length, right - left + 1)
            
#         return max_length

# results = Solution()
# ans = results.lengthOfLongestSubstring(s="abcabcbb")
# print(f"Length of longest substring: {ans}")
# _______________________________
