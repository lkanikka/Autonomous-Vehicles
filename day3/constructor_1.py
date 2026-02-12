class parent():
    def __init__(label_attr): # constructor , label_attr is a label
        label_attr.offset = 5 # use the label to all variables in the class

    def measurement(self,data):
        self.length = self.offset + data
        return self.length

obj = parent()
out = obj.measurement(2)
print(out)
