class parent():
    def __init__(self): # by default this will run
        print("hello from constructor method")

    def a(self):
        print("hello from method a")

    def b(self):
        print("hello from method b")

def hanza():
    obj = parent()
    obj.b()

if __name__ == "__main__":
    hanza()
