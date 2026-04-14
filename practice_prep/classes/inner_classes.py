class Outer:
    def __init__(self):
        self.name = "Outer class"
    
    class Inner:
        def __init__(self, name):
            # You can use the passed 'name' or hardcode it
            self.name = name 
        
        def display(self):
            return "This is the inner class"

# 1. Instantiate the Outer class
outer = Outer()
print(outer.name)

# 2. Instantiate the Inner class through the Outer instance
# We must provide the 'name' argument required by Inner's __init__
inner = outer.Inner("Inner Class") 
print(inner.name)

# 3. Call the display method with ()
print(inner.display())

