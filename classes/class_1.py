class person():
    def __init__(self, name):
        self.name =name
    def talk(self):
        print(f"Hi I am {self.name}")
    

anil = person("anil reddy")
print(anil.name)
anil.talk()