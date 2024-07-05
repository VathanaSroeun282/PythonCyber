class myOOP1 : 
    myOop = "This is my first OOP"
    def __init__(self, name, age) : 
        self.name = name
        self.age = age
    def yourInfo (self) :
        print("Your Name is : " + self.name)
        print("Your Age  is : " + str(self.age))
myOP = myOOP1("Vathana", 12)
myOP.yourInfo();