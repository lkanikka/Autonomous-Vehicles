class parent(): #class name
    def sum(label_attr,a,b): # label_attr is a label
        label_attr.c = (a).__add__(b)
        return(label_attr.c)

obj = parent()
oup = obj.sum(5,10)
print(oup)


# rules for defining function within class
    # def func_name (label, input_attr1, input_attr2 ... )
    # c = 
