s = "babad"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        results = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                string = s[i : j+1]
                if string == string[::-1] and len(string) > len(results):
                    results = string
        return print(results)
ans = Solution()
result = ans.longestPalindrome(s)
        