# def check_keyword(file_path, keyword):
#     try:
#         with open(file_path, 'r') as file:
#             for line_num, line in enumerate(file,1):
#                 if keyword.lower() in line.lower():
#                     return f"Found '{keyword}' on line {line_num}."
#         return f"Keyword '{keyword}' not found."
#     except FileNotFoundError:
#         return "Error: File not found."
# print(check_keyword("/home/mirafra/Desktop/python_learnings/Most_Asked_interview_qns/server.log", "ERROR"))


# keyword = "WORD"
# file_path = "/home/mirafra/Desktop/python_learnings/Most_Asked_interview_qns/server.log"
# with open(file_path, "r") as file:
#     for line in file:
#         if keyword.lower() in line.lower():
#             print(keyword)
#         else:
#             print("wordno ther!")

# text = "hi my name is prabas"
# list = text.split()
# for i in list:
#     if i == "my":
#         print("word is available")

text = "hi my name is prabas"

if "my" in text:
    print("word is available")