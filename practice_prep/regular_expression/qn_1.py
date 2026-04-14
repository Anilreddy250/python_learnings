import re

# results = re.match(r"hellow", "hellow world")
# if results:
#     print("match found:", results.group())
# text = "cat bat rat"
# matches = re.findall(r"\bat\b", text)
# print(matches)

# matches = re.findall(r"\w+at", text)
# print(matches)

# text = "hello world"
# result = re.sub(r"\s+", " ", text)
# print(result)

# text = "one1two2three3four"
# parts =re.split(r"\d", text)
# print(parts)

# pattern = re.compile(r"\d{3}-\d{4}")
# print(pattern.search("call 123-4567 now").group())

# def is_valid_email(email):
#     pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$"
#     return bool(re.match(pattern, email))
# print(is_valid_email("anil@gmail.com"))
# print(is_valid_email("invalid-email"))

# text = "call us at 123-4567 or 987-6543"
# phones = re.findall(r"\d{3}-\d{4}", text)
# print(phones)

# def is_string_password(pwd):
#     pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"
#     return bool(re.match(pattern, pwd))
# print(is_string_password("Passw0rd"))
# print(is_string_password("weakpass"))

text = "Visit https://www.example.com or http://example.org for more info."
urls =re.findall(r"https?://\S+", text)
print(urls)
