#determine if a string is a plaindrome (reads same foe)?
string = "abcdcba"
if string == string[::-1]:
    print("it's a palindrome")
else:
    print("Not A polindrome")