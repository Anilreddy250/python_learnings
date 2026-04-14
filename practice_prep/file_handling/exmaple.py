import csv
from io import stringIO


path = "/home/mirafra/Desktop/python_learnings/file_handling/demofile.txt"

# with open(path, "a+") as f:
#     # for x in f:
#     #     print(x)

#     f.write("now the file has more content")
#     f.seek(0)
# # with open("/home/mirafra/Desktop/python_learnings/file_handling/demofile.txt", "r") as f:
#     print(f.read())
r = csv.reader(stringIO(path))
for row in r:
    print(row)