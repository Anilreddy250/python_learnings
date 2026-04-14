text =str(input("enter the sentence :"))
vowels = "aeiou"
count = 0
# count = sum(1 for char in text if char.lower() in "aeiou")
# print(f"vowel:{count}")
for j in vowels.lower():
        
    for i in text.lower():
        if i == j in vowels:
            count +=1
            # print(count)
            # print("vowel")
print(count)