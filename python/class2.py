class MyClass:
    name = None
    marks = None

    def_init_(self, name, marks=0):
      print('hello  from constructor')
      self.name = name
      self.marks = marks
    
   def hello(self):
    print('hello,', self.name)
obj = MyClass("varsha")

obj = MyClass("Person",80)
