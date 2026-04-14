# from collections import defaultdict
# def group_anagrams(words):
#     anagram_map = defaultdict(list)
#     for word in words:
#         key = tuple(sorted(word))
#         anagram_map[key].append(word)
#     return list(anagram_map.values())
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_anagrams(words))

def sort_word(word):
    chars = list(word)
    n = len(chars)
    for i in range(n):
        for j in range(0, n-i-1):
            if chars[j]>chars[j+1]:
                chars[j],chars[j+1] = chars[j+1], chars[j]
    return "".join(chars)
def group_anagrams(words):
    anagram_map = {}
    for word in words:
        key = sort_word(word)
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(word)
    return list(anagram_map.values())
print(group_anagrams(words))

