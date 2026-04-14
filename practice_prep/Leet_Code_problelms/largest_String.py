class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        # Use the length of the shorter word to avoid IndexErrors
        for i in range(min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])
        
        # Add the remaining suffix from the longer word
        return "".join(res) + word1[i+1:] + word2[i+1:]
ans = Solution()
results = ans.mergeAlternately(word1="abc",word2="pqr")
print(results)