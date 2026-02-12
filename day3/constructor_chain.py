class parent():
    def __init__(self): # by default this will run
        print("hello from constructor parent method")

    def a(self):
        print("hello from method a")

class child(parent):
    def __init__(self): # by default this will run
        super().__init__() # constructor chaining
        print("hello from constructor child method")

    def b(self):
        print("hello from method b")


obj = child()
obj.a()
