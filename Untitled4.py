class Human:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
         
class Student(Human):
    pass 

class Undergraduate(Student):
    pass  
class ExchangeStudent:
    def __init__(self, xx, xy):
        self.xx = xx
        self.xy = xy

class InternationalStudent(Undergraduate, ExchangeStudent):
    def __init__(self, name, nationality, xx, xy):
        
        Undergraduate.__init__(self, name, nationality)
        ExchangeStudent.__init__(self, xx, xy)


student = InternationalStudent("Baran", "Türk", "Türkiye", 19)
print(student.name)         # Baran
print(student.nationality)  # Türkiye
print(student.xx)           # Türk
print(student.xy)           # 19
