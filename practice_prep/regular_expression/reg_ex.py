import re
txt = "the rain in spain"
# x =re.search("^the.*spain$", txt)
x =re.search("the", txt)

if x :
 print ("yes, we have a match")
else:
 print ("not a match")