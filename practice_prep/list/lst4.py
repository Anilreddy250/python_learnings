# sentence = "mokalla anil reddy"
# words = sentence.split()
# reversed_words = words[::-1]
# result = " ".join(reversed_words)
# print(result)

# raw_names = "alice, bob, charlice"
# clean_names = [name.strip().capitalize() for name in raw_names.split(",")]
# for index, name in enumerate(clean_names, start=1):
#     print(f"{index}, {name}")

# list = [1,2,3,4,5,6,7]
# reverse = list.reverse()
# print(reverse)

# string = "anianilaaaaaaaa"
# counts = string.find("l")
# print(counts)

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        print( a)
fibonacci_iterative(5)