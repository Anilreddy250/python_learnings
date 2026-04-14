class Bank:
    def __init__(self):
        self.__secret = "1234"

account = Bank()
# print(account.__secret)  # This will throw an ERROR!
print(account._Bank__secret) # This WORKS (but you shouldn't do it).