text = """
python is great for automation python is also great for data analysis
building a tool with python is fun and python is very popular
"""
words = text.lower().split()# turn the string into a list of words
counts = {}

for word in words:
    if word in counts:
        counts[word] +=1
    else:
        counts[word] = 1
# sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
for word, count in counts.items():
    print(f"{word}:{count}")
    # print(f"counts")