class math:
    def add(self):
        self.a = 5 #object variable, accessible in all methods
        self.b = 3 #object variable, accessible in all methods
        c = self.a + self.b # c -> local, temporary inside this method only
        return c

    def sum(self, d):
        # d is local parameter, temporary inside this method only
        summa = self.a + self.b + d # summa - > local, temporary inside this method only
        return summa


obj = math()
print(obj.add())  #output 8
print(obj.sum(2)) #output 10
