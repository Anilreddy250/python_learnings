#dictionary deep analysis
#How do you merge two dictionaries? if they share a key, which value is kept?
# in python 3.p+ the merge (|) and "Update"(|=) operators are preferred
# 
dict1 = {"env": "QA", "timeout": 30}
dict2 = {"timeout": 60, "browser": "Chrome"}

merged = dict1 | dict2 
print(merged)
# merged = {'env': 'QA', 'timeout': 60, 'browser': 'Chrome'}

# Rule: the value from the second dictionary (the one on the right) always overwrite the fisrt one
