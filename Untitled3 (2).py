class Phone:
    
    def __init__(self, color, brand, password):
        self.color = color                     # public instance variable
        self._brand = brand                    # protected instance variable 
        self.__password = password             # prıvate instance variable 
     
    def call(self): # instance method
        return "The " +self.color+"" +self._brand+ " ıs rınging"
    
person1= Phone("Black ", "Apple Phone", "Hıgly confıdentıal" )
person2= Phone("White", "Samsung Phone", "Top Secrete")
p1= Phone ("red", "Redmi Phone", "xxxxx")
print(person1.color)
print(person2._brand)
print(p1._Phone__password)

print(person1.call())