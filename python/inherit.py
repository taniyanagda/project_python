class MyClass:
    name = None
    marks = None

    def_init_(self, name, marks=0):
        print('hello from constructor')
        self.name = name 
        self.marks = marks
        self.hello()

    def hello(self):
        print('hello, ', self.name)
    def_repr_(self):
       return self.name


obj = MyClass('varsha')
print(obj)

obj1 = MyClass('rm')
print(obj1)
    