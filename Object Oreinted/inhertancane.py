class ParentOne:
    def Test_fuction(self):
        print("I am parentOne test fucntion") 
    def parent_one_fuction(self):
        print("THIS IS PARENT ONE TEST FUNCITON")

class ParentTwo:
    def Test_fuction(self):
        print("I am parentTwo")

class Child(ParentOne, ParentTwo):
    def show(self):
        print("I am child")

child = Child()
child.show()