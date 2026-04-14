# list&string (Data manipulation)
#how do you remove all duplicates from l list while 

items = ["apple", "orange","apple","banana"]

unique_items = list(dict.fromkeys(items))
print(f"{unique_items}")
