#common automation scenario
#How do you convert two lists (one containg "Headers" and one containg "Row valeus" from a csv)into a dictionary
headers = ["ID", "Name", "Status"]
values = [101, "Login_Test", "Pass"]

test_date = dict(zip(headers, values))
print(test_date)