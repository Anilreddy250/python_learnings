#the word frequency counter
#the problem write a script to read a text file, count how many times each word appears, and return the top 3 most common words?
# from collections import Counter
# import re
# def top_words(filepath, top_n=6):
#     try:
#         with open(filepath, 'r', encoding='utf-8') as file:
#             text = file.read().lower()
#             #use regex to extract words (ignores punctuation)
#             words = re.findall(r'\b\w+\b', text)
#             print(words)
#             #count the words
#             word_counts = Counter(words)
#             return word_counts.most_common(top_n)
        
#     except FileNotFoundError:
#         return "Error: File not found"

# filepath = "/home/mirafra/Desktop/python_learnings/storage_test.log"
# # result = top_words(filepath, 3)
# # print(result)

# # finding the longest word in a file 
# # the problem read file and find the longest word within it ?
# def find_longest_word(filepath):
#     longest_word = "" 
#     try :
#         with open(filepath,'r',encoding='utf-8')as file:
#             for line in file:
#                 words = line.split()
#                 for word in words:
#                     #strip punctuation for an accurate length check
#                     clean_word = word.strip(".,!?:;`\"")
#                     if len(clean_word) > len(longest_word):
#                         longest_word = clean_word
#         return longest_word
#     except FileExistsError:
#         return "File not found."
# results = find_longest_word(filepath)
# print(results)


# class Solution:
#     def longestWord(self, words):
#         words_set = set(words)
#         longest = ""
#         for word in words:
#             if len(word) < len(longest) or (len(word) == len(longest) and word > longest):
#                 continue
#             valid = True
#             for i in range(1, len(word)):
#                 if word[:i] not in words_set:
#                     valid = False
#                     break
#             if valid:
#                 longest = word
#         return longest

# if __name__ == '__main__':
#     dictionary_words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
#     result = Solution().longestWord(dictionary_words)
#     print("Longest word:", result)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        dsu = DSU(10001) # Max possible unique emails across all accounts
        email_to_id = {}
        email_to_name = {}
        id_counter = 0
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = id_counter
                    email_to_name[email] = name
                    id_counter += 1
                # Union the first email of this account with the current email
                dsu.union(email_to_id[account[1]], email_to_id[email])
        
        # Group emails by their DSU root
        merged = {}
        for email, eid in email_to_id.items():
            root = dsu.find(eid)
            if root not in merged:
                merged[root] = []
            merged[root].append(email)
            
        # Format the result: [Name, sorted_emails...]
        result = []
        for root, emails in merged.items():
            name = email_to_name[emails[0]]
            result.append([name] + sorted(emails))
            
        return result