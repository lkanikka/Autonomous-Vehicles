#polymorphism example
class parent_cls:
    def a(self):
        print("hello from a")

class child_cls():
    def a(self):
        print("hello from b")

class grandchild_cls():
    def a(self):
        print("hello from c")

obj_gc = grandchild_cls()
obj_gc.a()
