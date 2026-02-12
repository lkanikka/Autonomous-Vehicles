class parent:
        def a(self):
            print("hello from dunder_1")

def hanza():
        print("hello from main_logic")

# check if you are executing current file or just calling a class from a different file
if __name__ == "__main__":
    hanza()
