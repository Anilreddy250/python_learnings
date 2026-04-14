# count = 5
# while count > 0:
#     print(f't-minus{count}...')
#     count = count -1 # crucial this changes the condition!
# print("blast off !!")

# while True:
#     # print("iam stuk")
#     # pass

password = input("enter password:")
p = "AnilReddy"

while p == password:
    print("correct password")
    break
else:
    print("wrong password")