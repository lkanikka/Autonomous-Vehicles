#inheritance example
class parent_cls:
    def a(self):
        print("hello from a")

class child_cls(parent_cls):
    def b(self):
        print("hello from b")

class grandchild_cls(child_cls):
    def c(self):
        print("hello from c")

obj_gc = grandchild_cls()
obj_gc.a()
obj_gc.b()
obj_gc.c()
